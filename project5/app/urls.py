from django.urls import path
from app.views import *

urlpatterns = [
    path('register/',register,name='register')
]