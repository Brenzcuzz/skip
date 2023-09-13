from django.shortcuts import render
from .models import Mymodel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def save_data(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        Mymodel.objects.create(username=username, password=password)

        return render(request, 'error.html')