from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    roll= serializers.IntegerField()
    birthday = serializers.DateField()
    age = serializers.IntegerField()