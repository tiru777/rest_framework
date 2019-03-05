from rest_framework import serializers
from django.contrib.auth.models import User, Group
"""
    default authenticated user and group
"""

from . models import Employee

class Employeeserializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
