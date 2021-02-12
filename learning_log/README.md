# Learning Log

## Creating a Virtual

```bash
python -m venv ll_env
```

## Activating the Virtual Environment

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

## Installing Django

```bash
pip install django
```

## Creating a Project in Django

```bash
django-admin startproject learning_log .
 ```

## Creating the Database

```bash
python manage.py migrate
```

## Viewing the Project

```bash
python manage.py runserver
```
