from django.db import models


# Create your models here.

class SafetyToolsCategory(models.Model):
    category_id = models.IntegerField()
    category_name = models.TextField(max_length=500)

    def __unicode__(self):
        return self.category_name


class SafetyToolsPost(models.Model):
    category_id = models.ForeignKey(SafetyToolsCategory)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=30000)
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
