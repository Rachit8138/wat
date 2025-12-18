STEP: I
---

#  Creating a New Django Project

This guide outlines the steps demonstrated in the transcript for creating and running your first Django project using the `django-admin` tool.

---

##  Getting Started

Django allows you to spin up a fully functional project within minutes using built-in commands.

### **Create a new Django project**

Use the following command:

```bash
django-admin startproject smartnotes .
```

* `django-admin` — Django’s command-line utility
* `startproject` — Creates a new project
* `smartnotes` — Name of the project
* `.` — Creates the project in the current directory

Running this command generates:

```
manage.py
smartnotes/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```

---

##  Project Structure

### **manage.py**

The main entry point of your project.
You’ll use it to:

* Run the development server
* Interact with the database
* Execute various Django commands

### **smartnotes folder**

Contains the core configuration files:

* **settings.py** – Global project settings (e.g., DEBUG, installed apps, middleware)
* **urls.py** – URL routing configuration
* **asgi.py / wsgi.py** – Deployment entry points

> ️ `DEBUG = True` indicates you're in development mode, so Django will show detailed error messages.

---

## ▶ Running the Development Server

Use the command:

```bash
python manage.py runserver
```

After running it, you will see:

* Django version (e.g., 3.2)
* Active settings module (`smartnotes.settings`)
* A development URL, typically:

  ```
  http://127.0.0.1:8000/
  ```

Click the link or paste it into your browser to see Django’s default landing page.

---

##
You have successfully:

* Created a Django project
* Understood its structure
* Launched your first development server
