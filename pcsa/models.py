from django.db import models

from django.core.validators import RegexValidator
from profiles.models import Pcuser


class PcsaPost(models.Model):
    owner = models.ForeignKey(Pcuser, null=False, related_name='powner')
    title = models.CharField(max_length=100, validators=[
                                      RegexValidator(
                                          r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                      )])
    description = models.TextField(max_length=30000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.user.username
        
    class Meta:
    	verbose_name = 'FirstAide Post'
    	verbose_name_plural = 'FirstAide Posts'
