from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin  
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
# here use classes to seperate maximum views
class StudentListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetriveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# # for the following we need seperate urls for every view so wo i don't like to use this 
# # Generic APIView and Model Mixins
# # # List Student Data
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request,  *args, **kwargs):    
#         return self.list(request, *args, **kwargs)
# # # Create Student
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# # Retrive Student Data
# class StudentRetrive(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# # Update Student Data
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# # Destroy data
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
