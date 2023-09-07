# Wiki Encyclopedia using Django

This Django-based web application simulates an online encyclopedia. Users can view, search, create, edit, and access random encyclopedia entries stored in Markdown format. This project was designed as part of a web development course assignment and exemplifies key Django features such as URL routing, views, and file storage.

## Project Structure

- `views.py`: This file contains the main logic of the application. It defines how the app responds to user requests.
- `urls.py`: This file configures URL patterns, linking URLs to their respective view functions.
- `util.py`: Contains utility functions for interacting with the encyclopedia entries, such as listing all entries, saving an entry, and retrieving an entry.

## Key Features

1. **Index Page (`views.index`)**:
   - Displays a list of all encyclopedia entries.
2. **Entry Page (`views.entry`)**:
   - Renders a specific encyclopedia entry using its title.
   - If an entry doesn't exist, an error message is displayed.
3. **Search Functionality (`views.search`)**:
   - Users can search for an encyclopedia entry.
   - If a direct match is found, they are redirected to the entry page.
   - If no direct match is found, a list of entries containing the search term is displayed.
4. **Create New Entry (`views.create`)**:
   - Users can create a new encyclopedia entry.
   - If an entry with the given title already exists, an error message is displayed.
5. **Edit Existing Entry (`views.edit`)**:
   - Users can edit the Markdown content of an existing entry.
6. **Random Entry (`views.random`)**:

   - Displays a random encyclopedia entry to the user.

7. **Markdown Processing**:
   - The `markdown2` library is used to convert the Markdown content of entries into HTML for rendering.

## Running the Application

Before running the application, ensure you have Django installed:

```bash
pip3 install django
```

To run the application:

```bash
python3 manage.py runserver
```

Now, open a web browser and navigate to `http://127.0.0.1:8000/` to access the Wiki Encyclopedia.
