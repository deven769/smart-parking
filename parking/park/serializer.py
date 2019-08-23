from rest_framework import serializers
from .models import User, Park, UserProfile, ParkSlot, Feasibility


class UserSerializer(serializers.ModelSerializer):

    class meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'fist_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):

    class meta:
        model = UserProfile
        fields = ('id', 'user', 'licence_image', 'photo', 'park')


class ParkSerializer(serializers.ModelSerializer):

    class meta:
        model = Park
        fields = '__all__'


class ParkSlotSerializer(serializers.ModelSerializer):

    class meta:
        model = ParkSlot
        fields = '__all__'


class FeasibilitySerializer(serializers.ModelSerializer):

    class meta:
        model = Feasibility
        fields = '__all__'
