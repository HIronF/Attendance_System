from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Attendance_System import Student


@login_required(login_url='/')
def Home(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def add_student(request):
    return render(request,'Hod/add-student.html')

@login_required(login_url='/')
def add_teacher(request):
    return render(request,'Hod/add-teacher.html')

@login_required(login_url='/')

def view(request):
    return render(request,'Hod/view_student.html')

@login_required(login_url='/')

def edit(request,id):
    student = Student.objects.filter(id=id)

    context = {
        'student':student,
    }
    return render(request,'Hod/edit_student.html')


def view_teacher(request):
    return render(request,'view_teacher.html')