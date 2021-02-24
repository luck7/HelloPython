# Learning Log

## Setting Up a Project

### Creating a Virtual

```bash
python -m venv ll_env
```

### Activating the Virtual Environment

Linux

```bash
source ll_env/bin/activate
```

Windows

```bash
ll_env\Scripts\activate
```

```bash
deactivate
```

### Installing Django

```bash
pip install django
```

### Creating a Project in Django

```bash
django-admin startproject learning_log .
 ```

### Creating the Database

```bash
python manage.py migrate
```

### Viewing the Project

```bash
python manage.py runserver
```

## Starting an App

```bash
python manage.py startapp learning_logs
```

### Defining Models

### Activating Models

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

### The Django Admin Site

#### Setting Up a Superuser

```bash
(ll_env)learning_log$ python manage.py createsuperuser
Username (leave blank to use 'eric'): ll_admin
Email address:
Password:
Password (again):
Superuser created successfully.
(ll_env)learning_log$
```

#### Registering a Model with the Admin Site

#### Adding Topics

### Defining the Entry Model

### Migrating the Entry Model

```bash
(ll_env)learning_log$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
 learning_logs/migrations/0002_entry.py
 - Create model Entry
(ll_env)learning_log$ python manage.py migrate
Operations to perform:
 --snip--
Applying learning_logs.0002_entry... OK
```

### Registering Entry with the Admin Site

### The Django Shell

```bash
(ll_env)learning_log$ python manage.py shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
```

Each time you modify your models, you’ll need to restart the shell to see the effects of
those changes. To exit a shell session, press ctrl-D; on Windows, press ctrl-Z and
then press enter.

## Making Pages: The Learning Log Home Page

### Mapping a URL

### Writing a View

### Writing a Template

## Building Additional Pages

### Template Inheritance

### The Topics Page

### Individual Topic Pages

## Allowing Users to Enter Data

### Adding New Topics

### Adding New Entries

### Editing Entries

## Setting Up User Accounts

### The users App

### The Login Page

### Logging Out

### The Registration Page

## Allowing Users to Own Their Data

### Restricting Access with @login_required

### Connecting Data to Certain Users

### Restricting Topics Access to Appropriate Users

### Protecting a User’s Topics

### Protecting the edit_entry Page

### Associating New Topics with the Current User

## Styling Learning Log

### The django-bootstrap4 App

```bash
(ll_env)learning_log$ pip install django-bootstrap4
```
