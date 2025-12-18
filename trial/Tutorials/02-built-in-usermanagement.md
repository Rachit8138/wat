# Django Built-in User Management Tutorial

Django comes with a powerful built-in user authentication system that handles user accounts, groups, permissions, and cookie-based user sessions. This tutorial will guide you through setting up and using Django's user management features.

## Prerequisites

- Django project created
- Virtual environment activated
- Basic understanding of Django models and views

## Step 1: Database Migration

First, apply the initial migrations to create the necessary database tables for user management:

```bash
python manage.py migrate
```

This creates tables for:
- User accounts
- Groups
- Permissions
- Sessions

## Step 2: Create a Superuser

Create an admin user to access Django's admin interface:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username
- Email address (optional)
- Password

## Step 3: Start the Development Server

```bash
python manage.py runserver
```

Now you can access:
- Admin interface: `http://127.0.0.1:8000/admin/`
- Your application: `http://127.0.0.1:8000/`

## Step 4: Configure URLs for Authentication

Add authentication URLs to your main `urls.py`:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # Your app URLs here
]
```

This provides built-in views for:
- `/accounts/login/`
- `/accounts/logout/`
- `/accounts/password_change/`
- `/accounts/password_reset/`

## Step 5: Create Authentication Templates

Create a `registration` directory in your templates folder:

```
templates/
└── registration/
    ├── login.html
    ├── logout.html
    └── base.html
```

### Login Template (`templates/registration/login.html`):

```html
{% extends 'registration/base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<p><a href="{% url 'password_reset' %}">Forgot password?</a></p>
{% endblock %}
```

### Base Template (`templates/registration/base.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}User Management{% endblock %}</title>
</head>
<body>
    <nav>
        {% if user.is_authenticated %}
            <p>Welcome, {{ user.username }}! 
            <a href="{% url 'logout' %}">Logout</a></p>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
        {% endif %}
    </nav>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

## Step 6: Using Authentication in Views

### Protecting Views with Login Required:

```python
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
```

### Class-Based Views:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
```

## Step 7: User Registration (Custom View)

Create a simple registration view:

```python
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

### Registration Template:

```html
{% extends 'registration/base.html' %}

{% block title %}Register{% endblock %}

{% block content %}
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
{% endblock %}
```

## Step 8: Settings Configuration

Add these settings to your `settings.py`:

```python
# settings.py

# Redirect URLs after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Login URL for @login_required decorator
LOGIN_URL = '/accounts/login/'
```

## Key Features of Django's User System

### User Model Fields:
- `username`: Required, unique
- `email`: Optional
- `first_name`, `last_name`: Optional
- `is_active`: Boolean, default True
- `is_staff`: Can access admin
- `is_superuser`: Has all permissions
- `date_joined`: Auto-set on creation



## Testing Your Setup

1. Run the server: `python manage.py runserver`
2. Visit `/admin/` and login with your superuser account
3. Create some test users in the admin
4. Test login/logout functionality
5. Try accessing protected views

## Next Steps

- Customize the User model with a custom user model
- Add user profiles with additional fields
- Implement email verification
- Add social authentication
- Create user groups and permissions

## Common Issues

- **Template not found**: Ensure templates are in `templates/registration/`
- **CSRF token missing**: Always include `{% csrf_token %}` in forms
- **Redirect loops**: Check `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`

