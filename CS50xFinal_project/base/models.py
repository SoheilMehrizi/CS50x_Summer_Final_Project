from django.db import models
from django.db.models.fields import EmailField 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Create your models here.
class AboutMe(models.Model):
    Bio = models.TextField(max_length=200)
    image_address = models.CharField(max_length=50)


class specialities(models.Model):
    name         = models.CharField(max_length=15)
    Date_Of_earn = models.DateField(auto_now=False, auto_now_add=False)
    Description  = models.TextField(max_length=200)


class Experiences(models.Model):
    name         = models.CharField(max_length=15)
    Date_Of_Earn = models.DateField(auto_now=False, auto_now_add=False)
    Description  = models.TextField(max_length=200)


class Academy(models.Model):
    name               = models.CharField(max_length=15)
    Degree             = models.CharField(max_length=15)
    Date_Of_Graduation = models.DateField(auto_now=False, auto_now_add=False)
    Description        = models.TextField(max_length=200)



class contact(models.Model):
    Email   = models.EmailField()
    name    = models.CharField(max_length=15)
    Message = models.TextField(max_length=300)

class Economy(models.Model):
    user               = models.OneToOneField(User, on_delete=models.CASCADE)
    Description        = models.TextField(max_length=200)
    category           = models.CharField(max_length=20)
    Amount             = models.PositiveIntegerField()


class ToDoer(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    Task          = models.CharField(max_length= 20) 
    Task_category = models.CharField(max_length= 20)
    Deadline      = models.DateField(auto_now=False, auto_now_add=False)
    Description   = models.TextField(max_length=200)
