from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def terminalhome(request):
    return render(request, 'terminal_theme.html')

def terminaldashboard(request):
    return render(request, 'terminal_dashboard.html')
