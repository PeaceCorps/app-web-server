from django.db import models
from django.contrib.auth.models import User
import os
 
 
# Django provides a table called user that stores basic user information like username, password and email id.
class Pcuser(models.Model):
    #username
    user = models.OneToOneField(User)
    #location
    location = models.CharField(max_length=300)
    #phone number
    phone = models.CharField(max_length=150)
    #gender
    gender = models.CharField(max_length=10)
    #for reset_password
    reset_pass = models.CharField(default="",max_length=320)
     
    #verification status
    #1 - unverified
    #any other number = verification code
    verified = models.CharField(max_length=100)
     
    def __unicode__(self):
        return self.user.username