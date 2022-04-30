from dataclasses import fields
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = (
            'departmentId', 'departmentName'
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'employeeId', 'employeeName', 'department', 'dateOfJoining', 'photoFileName'
        )