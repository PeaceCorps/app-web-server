from django.db import models
from django.core.validators import RegexValidator
from profiles.models import Pcuser
from django.db.models.signals import post_save
from django.dispatch import Signal

post_update = Signal()


# Model for categories to be defined on the admin side
class SafetyToolsCategory(models.Model):
    category_id = models.IntegerField()
    category_name = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name
        
    class Meta:
    	verbose_name = 'Safety Tools Category'
    	verbose_name_plural = 'Safety Tools Categories'


class SafetyToolsPost(models.Model):
    category_id = models.ForeignKey(SafetyToolsCategory)
    title = models.CharField(max_length=500, validators=[
                                            RegexValidator(
                                                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                            )])
    description = models.TextField(max_length=30000)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # To get the url of the model in templates
    def get_absolute_url(self):
        return '/safetytools/view_post/%i' %self.id

    # To access the model name in templates
    def model_name(self):
        return 'PCSA Safety Tools Post'
        
    class Meta:
    	verbose_name = 'Safety Tools Post'
    	verbose_name_plural = 'Safety Tools Posts'


class safetyRevPost(models.Model):
    # The post which is being edited
    owner_rev_post = models.ForeignKey(SafetyToolsPost,
                                       null=False,
                                       related_name='owner_rev_post')
    # Revised title
    title_post_rev = models.CharField(max_length=1000)
    # Revised description
    description_post_rev = models.TextField(max_length=20000,
                                            validators=[
                                                RegexValidator(
                                                    r'^[(A-Z)|(a-z)|(0-9)|(\n)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                                )]
                                            )


    # Field to note the timestamp when the revised version was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner_rev.user.username
        
    class Meta:
        verbose_name = 'Safety Tools Reviewed Post'
        verbose_name_plural = 'Safety Tools Reviewed Posts'


# Signal to RevPost whenever a new post is created or updated
def create_revpost(sender, instance, created, **kwargs):
    safetyRevPost.objects.create(owner_rev_post=instance,
                      title_post_rev=instance.title,
                      description_post_rev=instance.description)


post_save.connect(create_revpost, sender=SafetyToolsPost)
post_update.connect(create_revpost, sender=SafetyToolsPost)
