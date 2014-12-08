from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def enlight_index(request):
    return render(request, 'enlight_base.html')


