from django.shortcuts import render
from app.models import *

# Create your views here.

def jsp(request):

    lod=Dept.objects.all()

    d={'dept':lod}

    return render(request,'jsp.html',d)

def qsp(request):

    loe=Emp.objects.all()

#field lookups
    #loe=Emp.objects.filter(sal__gt='2000')
    #loe=Emp.objects.filter(sal__lt='2000')
    #loe=Emp.objects.filter(deptno__gte='20')
    #loe=Emp.objects.filter(mgr__lte='7648')
    #loe=Emp.objects.filter(hiredate__lt='2020-06-16')

    #loe=Emp.objects.filter(hiredate__month='04')
    #loe=Emp.objects.filter(hiredate__year='2023')
    #loe=Emp.objects.filter(hiredate__day='23')
    #loe=Emp.objects.filter(job__startswith='m')
    #loe=Emp.objects.filter(ename__endswith='er')
    #loe=Emp.objects.filter(deptno__in=('10','20'))
    #loe=Emp.objects.filter(ename__contains='k')
    #loe=Emp.objects.filter(ename__regex='[A-za-z]{4}')

    
    d={'emp':loe}

    return render(request,'qsp.html',d)

    