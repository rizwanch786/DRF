from django.urls import path
from .views import *
urlpatterns = [
    path('stdapi/', StudentListCreate.as_view()),
    path('stdapi/<int:pk>', StudentRetriveUpdateDelete.as_view())
    # path('stuapi/',StudentList.as_view()),
    # path('stuapi/',StudentCreate.as_view()),
    # path('stuapi/<int:pk>',StudentRetrive.as_view()),
    # path('stuapi/<int:pk>',StudentUpdate.as_view()),
    # path('stuapi/<int:pk>',StudentDestroy.as_view()),
    # path('stuapi/<int:pk>',StudentList.as_view()),
]
