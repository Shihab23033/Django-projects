# Django To-Do List Application

A web-based To-Do List app built with Django, MySQL, and Pipenv.

- Add, update, and soft delete tasks (deleted tasks can be restored)
- View delete history (see all deleted tasks)
- Restore deleted tasks from history
- Permanently delete tasks from delete history
- Add, update, and soft delete tasks (deleted tasks can be restored)
- View delete history (see all deleted tasks)
- Restore deleted tasks from history
- Mark tasks as complete/incomplete
- Sort tasks by deadline, name, or created date (ascending/descending)
- Search tasks by name or description (with highlighted matches)
- AJAX for dynamic updates (no page reload)
- Bootstrap for a modern UI

## Requirements
- Python 3.8+
- pipenv
- MySQL Server
- MySQL client libraries (e.g., `mysqlclient`)

## Setup Instructions

### 1. Clone the repository and navigate to the project folder

```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Install Python dependencies using Pipenv

```
pipenv install --dev
```

### 3. Install MySQL Server
- Download and install MySQL from https://dev.mysql.com/downloads/installer/
- Start the MySQL server.

### 4. Create the MySQL database

Run the following SQL in your MySQL client:

```sql
CREATE DATABASE todolist_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON todolist_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

> **Note:** Update the username and password in `todolist/settings.py` if you use different credentials.

### 5. Run migrations

```
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)

```
pipenv run python manage.py createsuperuser
```

### 7. Run the development server

```
pipenv run python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Other Notes
- All dependencies are listed in `Pipfile` and `Pipfile.lock`.
- For any issues, check your MySQL server is running and credentials are correct.


## Project Structure
- `todolist/` - Project settings and URLs
- `todo/` - Main app (models, views, templates)
- `manage.py` - Django management script

---



## Usage

- The main page shows all active (not deleted) tasks.
- Use the sort controls to order tasks by deadline, name, or created date.
- Use the search box to filter tasks by name or description. Matching text will be highlighted.
- Click "Show Delete History" to view deleted tasks.
- On the delete history page:
	- Click "Restore" to bring a task back to the main list.
	- Click "Delete Permanently" to remove a task forever from the database.

---

**Enjoy your To-Do List app!**
