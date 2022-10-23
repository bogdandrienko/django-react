from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'django_app/home.html')
