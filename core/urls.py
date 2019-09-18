from django.urls import path
from .views.home import home, contact

urlpatterns = [
  path('home/', home, name='home'),
  path('contact/', contact, name='contact'),
]