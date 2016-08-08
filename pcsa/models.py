from django.db import models
from signup.models import Pcuser


class PcsaPost(models.Model):
    owner = models.ForeignKey(Pcuser, null=False, related_name='powner')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=30000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.owner.user.username