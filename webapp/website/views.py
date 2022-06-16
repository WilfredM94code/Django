from django.shortcuts import render

# Create your views here.

from app_2.models import App2

def welcome (resquest):
    variables = {
        'message': 'Beautiful static variable',
        'num_meetings' : App2.objects.count(),
        'meetings' : App2.objects.all()
    }
    return render(resquest,'website/home.html',variables)
