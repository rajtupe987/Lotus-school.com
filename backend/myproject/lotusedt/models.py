from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class StudentModel(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),

    ]
    
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    pass_hash = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.name

from django.db import models



class Expertise(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class Instructor(models.Model):
    expertise = models.ManyToManyField(Expertise)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructors = models.ManyToManyField(Instructor)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title