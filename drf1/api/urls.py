from django.urls import path
from .views import *
urlpatterns = [
    path('api/', student_api, name='std-api'),
    path('api/<int:pk>', student_api, name='std-api'),
]
