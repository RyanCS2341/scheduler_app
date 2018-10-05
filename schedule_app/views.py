from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'schedule_app/home.html')

def schedule(request):
    return render(request, 'schedule_app/schedule.html')
