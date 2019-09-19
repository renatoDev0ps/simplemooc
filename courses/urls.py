from django.urls import path
from .views.courses import *

urlpatterns = [
  path('courses/', courses, name='courses'),
  path('details/<slug:slug>', details, name='details'),
]