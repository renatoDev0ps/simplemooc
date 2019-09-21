from django.urls import path
from accounts.views import *

urlpatterns = [
  path('dashboard/', dashboard, name='dashboard'),
  path('edit_account/', edit_account, name='edit'),
  path('edit_password/', edit_password, name='password'),
  path('register/', register_user, name='register'),
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),
]
