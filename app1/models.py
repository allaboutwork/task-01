from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInstance(models.Model):
    # fields for UserInstance table
    pass

class Client(models.Model):
    name = models.CharField(max_length=100)
    user_instance = models.ForeignKey(UserInstance, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other')
    )
    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=LINK_CHOICES)
