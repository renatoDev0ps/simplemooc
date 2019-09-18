from django.urls import path
from .views.courses import *

urlpatterns = [
  path('courses/', courses, name='courses'),
  path('course/details/<int:id>', details, name='details'),
]