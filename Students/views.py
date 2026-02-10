from django.shortcuts import render,redirect,get_object_or_404
from Students.models import *
from Students.forms import *
# Create your views here.
def home(request):
    return render(request,'students/home.html')

def add_student(request):
    form=StudentForm()
    d={'form':form}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request,'students/add_student.html',d)

def student_list(request):
    students=Student.objects.all()
    d={'students':students}
    return render(request,'students/student_list.html',d)

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    d={'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'students/add_student.html',d)

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')