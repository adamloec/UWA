# UWApp
Universal Web Application (UWApp) is a template repository utilizing a Python Django backend and hosted on an Elastic Bean Stalk AWS server.

## Purpose
A personal template repository for all future web application development. Easy installation, setup, and configuration for all applications.

## Features
- Django backend: Custom user models, registration and login functionality, url management, views, and forms.
- Easy template customization and functionality, thanks to https://github.com/StartBootstrap/startbootstrap-sb-admin-2.
- Easily add accessory Django applications.

## Installation and Setup
1. Install the prerequisites for creating an Elastic Beanstalk AWS Django application:
    - Python 3.7 or later
```
pip install virtualenv awsebcli
``` 
2. Clone the UWApp repository:
```
git clone https://github.com/adamloec/UWApp
```
3. Create a virtual environment inside of the repository:
```
cd UWApp
virtualenv .venv
```
- To activate/deactivate:
```
.venv/Scripts/activate
deactivate
```
4. 