from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# class CustomUser(AbstractUser):

#     # add additional fields in here
#     licence_image = models.ImageField(upload_to='images/', blank=True)


class Park(models.Model):
    location = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    capasity = models.IntegerField()
    free_slots = models.IntegerField()
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.location


class User(AbstractUser):
    username = models.CharField(blank=True, max_length=100, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    licence_image = models.ImageField(upload_to='images/', blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True)
    park = models.ForeignKey(Park, related_name='_park',
                             on_delete=models.CASCADE)


# class UserLicence(models.Model):
#     licence_image = models.ImageField(upload_to='images/', blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     park = models.ForeignKey(Park, related_name='_park',
#                              on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class ParkSlot(models.Model):
    slot_number = models.IntegerField()

    park = models.ForeignKey(Park, related_name='parks',
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.slot_number) + ">" + str(self.park.location)


class Feasibility(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField()
    park_slot = models.ForeignKey(
        ParkSlot, related_name='slots', on_delete=models.CASCADE)

    def __str__(self):
        return "Feasibility"
