from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def home(request: HttpRequest):
    return render(request, 'main_app/index.html')
