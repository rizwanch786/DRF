from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
        
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
