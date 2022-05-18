from ast import Return
from functools import partial
from django.shortcuts import render
import pkg_resources
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['get', 'post', 'put', 'patch', 'delete'])
def student_api(request, pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)  
            serializer = StudentSerializer(std)
        else:
            std = Student.objects.all()
            serializer = StudentSerializer(std, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data = data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'message':'Record Created Successfully !!!'}, status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std, data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message':'Complete Record Update Successfully !!!'}, status=status.HTTP_200_OK)
        
    if request.method == 'PATCH':
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std, data = request.data, partial = True)
            if not serializer.is_valid():
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message':'Partial Record Update Successfully !!!'}, status=status.HTTP_200_OK)
        
    if request.method == 'DELETE':
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            std.delete()
            return Response({'message': 'Deleted Successfully'}, status = status.HTTP_200_OK)