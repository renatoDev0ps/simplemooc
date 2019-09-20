from django.urls import path
from accounts.views import *

urlpatterns = [
  path('login/', login_user, name='login'),
  path('register/', register_user, name='register'),
]
