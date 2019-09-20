from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings

from .forms import RegisterForm

# Create your views here.
def register_user(request):
  template_name = 'accounts/register.html'
  form_user = RegisterForm()
  if request.method == "POST":
    form_user = RegisterForm(request.POST)
    if form_user.is_valid():
      form_user.save()
      return redirect(settings.LOGIN_URL)
  else:
    form_user = RegisterForm()
  return render(request, template_name, {"form_user": form_user})

def login_user(request):
  template_name = 'accounts/login.html'
  form_login = AuthenticationForm()
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect(settings.LOGIN_REDIRECT_URL)
    else:
      messages.error(request, 'As credenciais estão incorretas!')
      return redirect(settings.LOGIN_URL)
  else:
    form_login = AuthenticationForm()
  return render(request, template_name, {"form_login":form_login})
