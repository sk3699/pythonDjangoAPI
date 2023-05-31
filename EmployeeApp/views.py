import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_ser = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_ser.data, safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        department_ser = DepartmentSerializer(data = department_data)
        if department_ser.is_valid():
            department_ser.save()
            return JsonResponse("Added Successfully!!!", safe = False)
        return JsonResponse("Failed to add data.", safe = False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_ser = DepartmentSerializer(department, data = department_data)
        if department_ser.is_valid():
            department_ser.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    elif request.method=='DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully!!!", safe = False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_ser = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_ser.data, safe=False)
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employee_ser = EmployeeSerializer(data = employee_data)
        if employee_ser.is_valid():
            employee_ser.save()
            return JsonResponse("Added Successfully!!!", safe = False)
        return JsonResponse("Failed to add data.", safe = False)
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_ser = EmployeeSerializer(employee, data = employee_data)
        if employee_ser.is_valid():
            employee_ser.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    elif request.method=='DELETE':
        employee = Employees.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!!", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe = False)