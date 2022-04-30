from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(departments_serializer.data, safe = False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department data added successfully", safe = False)
        return JsonResponse("Failed to add Department data", safe = False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        depId = department_data['departmentId']
        department=Departments.objects.get(departmentId=depId)
        departments_serializer=DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department data updated successfully", safe = False)
        return JsonResponse("Failed to update Department data", safe = False)
    elif request.method=='DELETE':
        department=Departments.objects.get(departmentId=id)
        department.delete()
        return JsonResponse("Department data deleted successfully", safe = False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employees_serializer.data, safe = False)
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee data added successfully", safe = False)
        return JsonResponse("Failed to add Employee data", safe = False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        depId = employee_data['employeeId']
        employee=Employees.objects.get(employeeId=depId)
        employees_serializer=EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee data updated successfully", safe = False)
        return JsonResponse("Failed to update Employee data", safe = False)
    elif request.method=='DELETE':
        employee=Employees.objects.get(employeeId=id)
        employee.delete()
        return JsonResponse("Employee data deleted successfully", safe = False)

@csrf_exempt
def saveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)