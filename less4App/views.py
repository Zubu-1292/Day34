from django.shortcuts import render, redirect
from .models import Employee
from less4App.forms import EmployeeForm

from django.core.paginator import Paginator
from django.contrib import messages

from less4App.forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
        emp = Employee.objects.all()
        context = {'title': 'Welcome', 'employees': emp}
        return render(request,"index.html",context)

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert Succesfully')
                return redirect('/')
            except:
                pass
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,"create.html",{'form':form})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES)
    return render(request,'edit.html', {'employee':employee, 'form':form})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES,instance=employee)
    if form.is_valid():
        try:
            form.save()
            messages.error(request,'Update Succesfully')
            return redirect('/')
        except:
            pass
        else:
            messages.error(request,form.errors)
    return render(request,"edit.html",{'employee':employee,'form':form})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect("/")

def test(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert Succesfully')
                return redirect('/')
            except:
                pass
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,"test.html",{'form':form})

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['to']
            message = form.cleaned_data['message']

            recipient_list = []
            recipient_list.append(from_email)
            try:
                emailobj = EmailMessage(subject, message, to=recipient_list)
                emailobj.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, "email.html", {'form': form})
