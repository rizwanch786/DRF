from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

class StudentApi(APIView):
    def get(self, request, pk = None, format = None):
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std)
        else:
            std = Student.objects.all()
            serializer = StudentSerializer(std, many = True)
        return Response(serializer.data)
    
    def post(self, request, pk = None):  # sourcery skip: class-extract-method
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'Message':'Record Saved Successfully..!!!'}, status = status.HTTP_201_CREATED)

    def put(self, request, pk = None):  # sourcery skip: class-extract-method
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std, data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'Message':'Complate Record Saved Successfully..!!!'}, status = status.HTTP_200_OK)
        
    
    def patch(self, request, pk = None):
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std, data = request.data, partial = True)
            if not serializer.is_valid():
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'Message':'Partial Record Saved Successfully..!!!'}, status = status.HTTP_200_OK)
        
    def delete(self, request, pk = None):
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            std.delete()
            return Response({'Message':'Record Deleted Successfully..!!!'}, status = status.HTTP_200_OK)

            