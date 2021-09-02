from django.shortcuts import render,HttpResponseRedirect
from . models import Employee
from . forms import EmployeeDetail
from django.contrib import messages
# Create your views here.

def showdata(request):
    if request.method == 'POST':
        fm = EmployeeDetail(request.POST)
        if fm.is_valid():

            nm = fm.cleaned_data['name']
            dp = fm.cleaned_data['department']
            ct = fm.cleaned_data['city']
            sl = fm.cleaned_data['salary']

            print(nm)
            print(dp)
            print(ct)
            print(sl)
           
            fm.save()
            fm = EmployeeDetail()
         
    else:        
        fm = EmployeeDetail()

    db = Employee.objects.all()
    return render(request, 'enroll/showdata.html',{'form':fm,'data':db})


def deletedata(request,id):
    if request.method=="POST":
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def editdata(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeDetail(request.POST,instance = pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Profile updated. Press "Go Back" ')
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeDetail(instance = pi)       
    return render(request,'enroll/editdata.html',{'form':fm})     