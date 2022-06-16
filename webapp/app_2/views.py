from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .forms import App2ModelForm
# Create your views here.

from .models import App2, App3

def details (resquest,id):
    detail = get_object_or_404 (App2, pk=id)
    variables = {
        'meeting': detail,
    }
    return render(resquest,'app_2/detail.html',variables)

def room_list (request):
    variables = {
        'rooms' : App3.objects.all(),
        'message' : 'Happily we provide the current rooms',
    }
    return render(request,'app_2/rooms.html',variables)

def room (request,id):
    detail = get_object_or_404 (App3, pk=id)
    variables = {
        'room' : detail,
    }
    return render(request,'app_2/room.html',variables)

def form(request):
    if request.method == 'POST':
        form = App2ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = App2ModelForm()
    variables = {
        'form' : form
    }
    return render(request,'app_2/form.html',variables)