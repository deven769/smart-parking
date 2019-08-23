from django.urls import path
from .views import *
app_name = 'park'


urlpatterns = [
    path('user/', UserView.as_view(), name='user'),

]
