# Django LMS Project

This is a Learning Management System (LMS) built with Django.

## Features
- User management
- Course management
- REST API endpoints (see `serlizers.py` and `views.py`)
- Admin interface

## Project Structure
```
LMS/                # Django project settings and configuration
courses/            # Main app for courses and users
    models.py       # Database models
    views.py        # API and web views
    serlizers.py    # DRF serializers
    urls.py         # App URL routes
    admin.py        # Admin registration
    tests.py        # Unit tests
    migrations/     # Database migrations
manage.py           # Django management script
db.sqlite3          # SQLite database (default)
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install django djangorestframework
   ```
3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
4. **Create a superuser**
   ```sh
   python manage.py createsuperuser
   ```
5. **Run the development server**
   ```sh
   python manage.py runserver
   ```
6. **Access the app**
   - Admin: http://127.0.0.1:8000/admin/
   - API endpoints: see `courses/urls.py`

