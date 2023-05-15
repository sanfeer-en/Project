from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'base.html')
def unit(request):
    return render(request, 'unitform.html')
