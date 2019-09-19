from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from ..forms import ContactCourse

# Create your views here.

def courses(request):
  courses = Course.objects.all()
  template_name = 'courses/index.html'
  return render(request, template_name, {"courses": courses})

def details(request, slug):
  # course = Course.objects.get(id=id)
  template_name = 'courses/details.html'
  course = get_object_or_404(Course, slug=slug)
  if request.method == "POST":
    form_contact = ContactCourse(request.POST)
    if form_contact.is_valid():
      name = form_contact.cleaned_data["name"]
      email = form_contact.cleaned_data["email"]
      message = form_contact.cleaned_data["message"]
      return redirect('courses')
  else:
    form_contact = ContactCourse()
  return render(request, template_name, {"course": course, "form_contact": form_contact})