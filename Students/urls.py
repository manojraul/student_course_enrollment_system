from Students.views import *
from django.urls import path
# app_name='student_app'
urlpatterns=[
    path('home/',home,name='home'),
    path('add_student/',add_student,name='add_student'),
    path('student_list/',student_list,name='student_list'),
    path('edit_student/<int:id>/',edit_student,name='edit_student'),
    path('delete_student/<int:id>/',delete_student,name='delete_student'),
] 