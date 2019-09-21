from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import RegisterForm, EditAccountForm

# Create your views here.
@login_required
def dashboard(request):
  template_name = 'accounts/dashboard.html'
  return render(request, template_name)
  
def register_user(request):
  template_name = 'accounts/register.html'
  form_user = RegisterForm()
  if request.method == "POST":
    form_user = RegisterForm(request.POST)
    if form_user.is_valid():
      user = form_user.save()
      user = authenticate(username=user.username, password=form_user.cleaned_data["password1"])
      login(request, user)
      return redirect(settings.LOGIN_REDIRECT_URL)
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

def logout_user(request):
  logout(request)
  return redirect(settings.LOGIN_REDIRECT_URL)

@login_required
def edit_account(request):
  template_name = 'accounts/edit.html'
  form_edit_account = EditAccountForm()
  context = {}
  if request.method == "POST":
    form_edit_account = EditAccountForm(request.POST or None, instance=request.user)
    if form_edit_account.is_valid():
      form_edit_account.save()
      form_edit_account = EditAccountForm(instance=request.user)
      context['success'] = True
  else:
    form_edit_account = EditAccountForm(instance=request.user)
  return render(request, template_name, {"form_edit_account": form_edit_account}, context)

@login_required
def edit_password(request):
  template_name = 'accounts/password.html'
  form_edit_password = PasswordChangeForm(user=request.user)
  context = {}
  if request.method == "POST":
    form_edit_password = PasswordChangeForm(data=request.POST, user=request.user)
    if form_edit_password.is_valid():
      form_edit_password.save()
      context['success'] = True
  else:
    form_edit_password = PasswordChangeForm(user=request.user)
  return render(request, template_name, {"form_edit_password": form_edit_password}, context)
