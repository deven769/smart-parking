from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.


class UserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class parkView(RetrieveUpdateDestroyAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer


class ParkSlotView(RetrieveUpdateDestroyAPIView):
    queryset = ParkSlot.objects.all()
    serializer_class = ParkSlotSerializer


class FeasibilityView(RetrieveUpdateDestroyAPIView):
    queryset = Feasibility.objects.all()
    serializer_class = FeasibilitySerializer
