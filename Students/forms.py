from django import forms
from Students.models import *
# ch=[('python','python'),('django','django'),('java','java')]
# class StudentForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     email=forms.EmailField()
#     age=forms.IntegerField()
#     courses=forms.MultipleChoiceField(choices=ch,widget=forms.CheckboxSelectMultiple)
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'courses': forms.CheckboxSelectMultiple
        }
