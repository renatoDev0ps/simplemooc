from django.shortcuts import render, get_object_or_404
from ..models import Course
# Create your views here.

def courses(request):
  courses = Course.objects.all()
  template_name = 'courses/index.html'
  return render(request, template_name, {"courses": courses})

def details(request, id):
  # course = Course.objects.get(id=id)
  course = get_object_or_404(Course, id=id)
  template_name = 'courses/details.html'
  return render(request, template_name, {"course": course})