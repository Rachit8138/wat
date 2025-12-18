# CSRF in Django

## What is CSRF?

**CSRF (Cross-Site Request Forgery)** is a security vulnerability where a malicious website tricks a logged-in user into performing actions on another site without their consent.

Examples of CSRF attacks:
- Submitting forms silently  
- Changing passwords or settings  
- Deleting data or performing destructive actions  

Django protects against CSRF using a **CSRF token**, a secret value that ensures the request truly originates from your website.

---

## How Django Protects You

Django automatically enables CSRF protection for unsafe HTTP methods:
- POST  
- PUT  
- PATCH  
- DELETE  

GET requests do **not** require CSRF because they must not modify data.

```html
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
    <button type="submit">Submit</button>
</form>
```
## Below is a simple visual model of how a CSRF attack works:

Attacker Site                Victim Browser                 Target Site (Your App)
--------------               ---------------                -------------------------
Malicious HTML Form  --->  User already logged in   --->   Receives request WITHOUT
auto-submits behind        to your website                  valid CSRF token → Rejects
the scenes                                                     (Django blocks it)


## With Django's CSRF token in place:
Legitimate Form ---> Browser ---> Server (CSRF Token Valid) → Action Allowed

## Where CSRF Tokens Are Used
```html
1. Django Templates
<form method="POST">
    {% csrf_token %}
</form>
```

2. AJAX Requests (Fetch API)

You must include the CSRF token in headers:

```python
fetch("/endpoint/", {
    method: "POST",
    headers: {
        "X-CSRFToken": csrftoken
    }
});
```

## When to Disable CSRF (Use With Extreme Caution)
from django.views.decorators.csrf import csrf_exempt

```python
@csrf_exempt
def my_view(request):
    return HttpResponse("CSRF disabled for this view")
```

## Only disable CSRF when:
Building public APIs<
- Using token-based authentication like JWT
- You fully understand the risks

## Without CSRF Protection

Without CSRF protection:

- Attackers can impersonate users  
- Session cookies become dangerous  
- Sensitive operations (such as password changes or posting data) become vulnerable  

CSRF protection is one of Django’s strongest features for maintaining secure web applications.
