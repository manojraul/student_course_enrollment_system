from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    mobile = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit Indian mobile number'
            )
        ]
    )
    courses=models.ManyToManyField(Course)
    def __str__(self):
        return self.name