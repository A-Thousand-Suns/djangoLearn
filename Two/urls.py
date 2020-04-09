from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^getstudents/', views.get_student)
]