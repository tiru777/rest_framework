from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import Employeeserializers, UserSerializers, GroupSerializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

class EmployeeList(APIView):
    def get(self,request):
        employee1 = Employee.objects.all()
        serializer = Employeeserializers(employee1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class UserViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows users to be viewed or edited
     """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializers

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows groups to bbe viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

