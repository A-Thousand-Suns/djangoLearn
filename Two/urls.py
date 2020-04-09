from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^getstudents/', views.get_student),
    url(r'^updatestudent/', views.update_student),
    url(r'^deletestudent/', views.del_student)
]