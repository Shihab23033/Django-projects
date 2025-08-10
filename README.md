# Django To-Do List Application

A web-based To-Do List app built with Django, MySQL, and Pipenv.

## Features
- Add, update, and delete tasks
- Mark tasks as complete/incomplete
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
- To install Node.js (optional, for advanced frontend tooling): https://nodejs.org/
- All dependencies are listed in `Pipfile` and `Pipfile.lock`.
- For any issues, check your MySQL server is running and credentials are correct.

## Project Structure
- `todo/` - Django app with models, views, templates
- `todolist/` - Project settings and URLs
- `manage.py` - Django management script

---

**Enjoy your To-Do List app!**
