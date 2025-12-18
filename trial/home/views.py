import datetime

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

'''Class-Based Views'''

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

class LogoutInterfaceView(LogoutView):
    #Subclass LogoutView and override post()
    #more secure way
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")  # or wherever you want

class HomeView(TemplateView):
    template_name = "home/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today()
        return context


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name = "home/signup.html"
    success_url="/login"


    #we are overriding the default validation for testing purpose
    def get_form(self,form_class=None):
        form=super().get_form(form_class)
        form.fields["username"].help_text=None
        form.fields["password1"].help_text=None
        form.fields["password2"].help_text=None
        return form

