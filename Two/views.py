from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse('two index')


def add_student(request):
    student = Student()
    student.s_name = 'Jerry'
    student.s_age = 19
    student.save()
    return HttpResponse('add success %s' % student.s_name)


def get_student(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    #return HttpResponse('students list')
    return render(request, 'student_list.html')