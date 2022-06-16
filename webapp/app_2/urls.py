from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.room_list, name = 'room_list'),
    path('rooms/<int:id>', views.room, name = 'room'),
    path('<int:id>', views.details, name = 'detail'),
    path('new_meeting', views.form, name = 'form'),
]
