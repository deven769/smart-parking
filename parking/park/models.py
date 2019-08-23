from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):

#     # add additional fields in here
#     licence_image = models.ImageField(upload_to='images/', blank=True)

class UserLicence(models.Model):
    licence_image = models.ImageField(upload_to='images/', blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Park(models.Model):
    location = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ParkSlot(models.Model):
    slot_number = models.IntegerField()
    free = models.BooleanField()
    occupied = models.BooleanField()
    park = models.ForeignKey(Park, related_name='parks',
                             on_delete=models.CASCADE)


class Feasibility(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField()
    park_slot = models.ForeignKey(
        ParkSlot, related_name='slots', on_delete=models.CASCADE)
