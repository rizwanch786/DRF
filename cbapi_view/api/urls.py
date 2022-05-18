from django.urls import path
from .views import *

urlpatterns = [
    path('api/', StudentApi.as_view(), name = 'std-api'),
    path('api/<int:pk>/', StudentApi.as_view(), name = 'std-api')
]
