from django.shortcuts import render
from django.http import JsonResponse
from firstapp.models import Employee


# Create your views here.

def employeeview(request):
    data = Employee.objects.all()
    response = {
        'employee': list(data.values('id', 'name', 'sal'))
    }
    return JsonResponse(response)
