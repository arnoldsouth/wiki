from django.shortcuts import redirect, render
from random import choice
import re
import markdown2

from . import util


def index(request):
    entries = util.list_entries()

    return render(request, "encyclopedia/index.html", {"entries": entries})


def entry(request, title):
    try:
        entry = markdown2.markdown(util.get_entry(title))

        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "entry": entry},
        )

    except FileNotFoundError:
        message = "The requested page was not found."

        return render(
            request,
            "encyclopedia/error.html",
            {"message": message},
        )


def search(request):
    # Get the search query param from the request
    title = request.GET["q"]

    entry = util.get_entry(title)
    if entry is not None:
        # Redirect to the entry page if the query matches an entry
        return redirect("entry", title=title)

    search_results = []

    entries = util.list_entries()
    for entry in entries:
        # Use re.search to find substrings
        if re.search(title, entry, re.IGNORECASE):
            search_results.append(entry)

    return render(
        request,
        "encyclopedia/search.html",
        {"title": title, "search_results": search_results},
    )


def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")

    else:
        title = request.POST["title"]

        # entries = util.list_entries()
        entries = [entry.lower() for entry in util.list_entries()]

        if title in entries:
            message = "This page has already been created."
            return render(
                request, "encyclopedia/error.html", {"message": message}
            )

        else:
            entry = request.POST["entry"]
            util.save_entry(title, entry)

    entries = util.list_entries()

    return render(
        request,
        "encyclopedia/index.html",
        {"entries": entries},
    )


def edit(request, title):
    # When user clicks "Edit" on the entry's page, render the original entry content
    if request.method == "GET":
        entry = util.get_entry(title)

        return render(
            request, "encyclopedia/edit.html", {"title": title, "entry": entry}
        )

    # Once user makes edits to the entry on this edit.html page and clicks "Save"
    else:
        edited_title = request.POST["title"]
        edited_entry = request.POST["entry"]

        util.save_entry(edited_title, edited_entry)

        return redirect("entry", title=edited_title)


def random(request):
    title = choice(util.list_entries())

    entry = markdown2.markdown(util.get_entry(title))

    return render(
        request,
        "encyclopedia/entry.html",
        {
            "title": title,
            "entry": entry,
        },
    )
