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

    context = {
        'hobby' : 'play games',
        'eat' : 'meat',
        'students' : students
    }
    return render(request, 'student_list.html', context=context)


def update_student(request):
    student = Student.objects.get(pk=1)
    student.s_name = 'marry'
    student.save()
    return HttpResponse('update success')


def del_student(request):
    student  = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse('delete student success')