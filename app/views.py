from django.shortcuts import render
from app.models import *

# Create your views here.

def jsp(request):

    lod=Dept.objects.all()

    d={'dept':lod}

    return render(request,'jsp.html',d)

def qsp(request):

    loe=Emp.objects.all()

    loe=Emp.objects.filter(ename__endswith='s')

    d={'emp':loe}

    return render(request,'qsp.html',d)

    