# DJANGO PROJECT - Employee Register CRUD

A Django-based Employee Register application with full CRUD operations, PostgreSQL integration, and a Bootstrap UI powered by Crispy Forms.

## Project Overview

This project helps manage employee records with a clean web interface. It supports creating, listing, editing, and deleting employee details and links each employee to a job position.

## Features

- Create employee records
- List all employee records
- Update employee information
- Delete employee records
- Position relation (`Employee -> Position`)
- Bootstrap 4 responsive templates
- Crispy Forms integration for better form rendering

## Tech Stack

- Python
- Django 6
- PostgreSQL
- django-crispy-forms
- crispy-bootstrap4
- Bootstrap 4
- HTML templates

## Routes

- `/employee/` -> create new employee
- `/employee/list/` -> view employee list
- `/employee/<id>/` -> update employee
- `/employee/delete/<id>/` -> delete employee
- `/admin/` -> Django admin panel

## Project Structure

```text
django project/
|-- manage.py
|-- webproject/
|   |-- settings.py
|   |-- urls.py
|   `-- ...
|-- employee_register/
|   |-- models.py
|   |-- views.py
|   |-- forms.py
|   |-- urls.py
|   |-- templates/employee_register/
|   |   |-- base.html
|   |   |-- employee_form.html
|   |   `-- employee_list.html
|   `-- migrations/
|-- .gitignore
|-- .env.example
|-- requirements.txt
`-- README.md
```

## Local Setup

1) Clone repository:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

2) Create and activate virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

3) Install dependencies:

```bash
pip install -r requirements.txt
```

4) Create `.env` from `.env.example` and fill real values.

5) Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6) Start server:

```bash
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/employee/list/`
- `http://127.0.0.1:8000/admin/`

## Environment Variables

Use these keys in `.env`:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

## Security Notes

- Do not commit `.env` to GitHub
- Do not hardcode credentials in `settings.py`
- Use `DJANGO_DEBUG=False` in production
- Rotate credentials if they were ever committed publicly

## Suggested Improvements

- Add authentication and role permissions
- Add pagination and search in employee list
- Add validation rules and tests
- Add CI checks (lint + tests) for quality

## Author

Your Name  
GitHub: https://github.com/<your-username>