from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.IntegerField()
    capacity = models.IntegerField()
    guests = models.IntegerField(default=0, null=True, blank=True)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)


class Reservations(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.start)