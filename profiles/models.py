import os

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage


# Django provides a table called user that stores basic user information like username, password and email id.
class Pcuser(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'), ('Restricted', 'Prefer not to say'))
    # Username
    user = models.OneToOneField(User)
    #location
    location = models.TextField(max_length=300, default='N.A.')
    #phone number
    phone_regex = RegexValidator(r'\+\d{8,15}$', message = "Phone number must have correct format. +999999 and up to 15 digits allowed")
    phone = models.CharField(validators=[phone_regex],blank=False, max_length=15 ,default='N.A.')
    #gender
    gender = models.CharField(max_length=10,choices = gender_choices, default='Restricted')
    #for reset_password
    reset_pass = models.CharField(default="",max_length=320)

    # Define the file storage system
    fs = FileSystemStorage(location='static/')
    # For user's display picture
    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/example.png',null=True)
     
    # Verification status
    # 1 - unverified
    # Any other number = verification code
    verified = models.CharField(max_length=100)
    
    # Name to be shown for a particular instanceof thistype of model 
    def __str__(self):
        return self.user.username
    
    # Name to be shown on the home page of the admin view for the collective set of model instances    
    class Meta:
    	verbose_name = 'Pcuser'
    	verbose_name_plural = 'Pcusers'


# Signal to create a corresponding pcuser whenever a user is created
def create_pcuser(sender, instance, created, **kwargs):
	if created:
		Pcuser.objects.create(user=instance)


# Call for pcuser creation after saving the user 
post_save.connect(create_pcuser, sender=User)