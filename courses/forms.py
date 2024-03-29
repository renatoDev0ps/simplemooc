from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template

class ContactCourse(forms.Form):
  name = forms.CharField(label='Nome', max_length=100)
  email = forms.EmailField(label='E-mail')
  message = forms.CharField(label='Mensagem/Dùvida', widget=forms.Textarea)
  
  def send_mail(self, course):
    subject = '[%s] contato' % course
    context = {
      'name': self.cleaned_data['name'],
      'email': self.cleaned_data['email'],
      'message': self.cleaned_data['message'],
    }
    template_name = 'courses/contact_email.html'
    send_mail_template(
      subject, template_name, context, 
      [settings.CONTACT_EMAIL]
    )
    
    # envio de email pelo console
    # send_mail(
    #   subject, message, settings.DEFAULT_FROM_EMAIL, 
    #   [settings.CONTACT_EMAIL]
    # )