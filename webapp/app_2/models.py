from django.db import models
from datetime import time
# Create your models here.


class App3(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    def __str__(self):
        return f'{self.name}: Room {self.room_number} on floor {self.floor}'

class App2(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(App3, on_delete = models.CASCADE)
    def __str__(self):
        return f'Meeting for {self.title} at {self.start_time} on {self.date}'
