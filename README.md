# UWApp
Universal Web Application (UWApp) is a template repository utilizing a Python Django backend and hosted on an Elastic Bean Stalk AWS server.

## Purpose
A personal template repository for all future web application development. Easy installation, setup, and configuration for all applications.

## Features
- Django backend: Custom user models, registration and login functionality, url management, views, and forms.
- Easy template customization and functionality, thanks to https://github.com/StartBootstrap/startbootstrap-sb-admin-2.
- SQLite database for all custom models and user information.
- Easily add accessory Django applications.

## Installation and Initial Setup
1. Install the prerequisites for creating an Elastic Beanstalk AWS Django application:
    - Python 3.7 or later
```
C:\> pip install virtualenv awsebcli
``` 
2. Clone the UWApp repository:
```
C:\> git clone https://github.com/adamloec/UWApp
```
3. Create a virtual environment inside of the repository:
```
C:\> cd UWApp\uwapp
C:\UWApp\uwapp> virtualenv .venv
```
4. Active the virtual environment and run the application locally:
```
C:\UWApp\uwapp> .venv/Scripts/activate
C:\UWApp\uwapp> python manage.py migrate
C:\UWApp\uwapp> python manage.py runserver
```
5. To close the server and virtual environment:
```
C:\UWApp\uwapp> CTRL^C
C:\UWApp\uwapp> deactivate
```
## Create new Django Applications and Customization
1. Create or add a new Django application inside of UWApp (Replace "new_app" with the name of the new application):
```
C:\UWApp\uwapp> python manage.py startapp new_app
```
2. Add the new application to INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uwapp',
    'new_app',
]
```
## AWS Elastic Beanstalk Configuration
1. Activate the virtual environment:
```
C:\UWApp\uwapp> .venv/Scripts/activate
```
2. 