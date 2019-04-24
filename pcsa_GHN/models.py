from django.db import models
from profiles.models import Pcuser
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage
from profiles.models import Pcuser
from django.db.models.signals import post_save
from django.dispatch import Signal

post_update = Signal()

class Contact(models.Model):
    office_name = models.CharField(max_length=200)
    contact_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r'^\+?[1-9]\d{1,14}$',
                message="Please enter a valid phone number. e.g. +44 7911 123456",
            ),
        ],
    )

    def __str__(self):
        return self.office_name

    def get_absolute_url(self):
        return '/gethelpnow/view_contact/%i' % self.id

    class Meta:
    	verbose_name = 'Contact'
    	verbose_name_plural = 'Contacts'


class ghnPost(models.Model):
    owner = models.ForeignKey(Pcuser, null=False, related_name='xowner')
    title = models.CharField(max_length=1000, validators=[
                                        RegexValidator(
                                            r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                        )])
    description = models.TextField(max_length=3000)
    created_date = models.DateTimeField(auto_now=True)

    # Link to important documents
    link = models.CharField(max_length=200, null = True)

    fs = FileSystemStorage(location='static/')

    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    def __str__(self):
        return self.title

    # To get the url of the model in templates
    def get_absolute_url(self):
        return '/gethelpnow/view_post/%i' % self.id

    # To access the model name in templates
    def model_name(self):
        return 'PCSA Get Help Now'

    class Meta:
    	verbose_name = 'Get Help Now Post'
    	verbose_name_plural = 'Get Help Now Posts'


class ghnRevPost(models.Model):
    # The post which is being edited
    owner_rev_post = models.ForeignKey(ghnPost,
                                       null=False,
                                       related_name='owner_rev_post')
    # The user who is editing the post
    owner_rev_ghn = models.ForeignKey(Pcuser, null=False, related_name='owner_rev_ghn')
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

    link_rev = models.CharField(max_length=200, null = True)

    fs = FileSystemStorage(location='static/')

    photo_rev = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)


    def __str__(self):
        return self.owner_rev.user.username

    class Meta:
        verbose_name = 'GHN Reviewed Post'
        verbose_name_plural = 'GHN Reviewed Posts'


# Signal to RevPost whenever a new post is created or updated
def create_revpost(sender, instance, created, **kwargs):
    ghnRevPost.objects.create(owner_rev_ghn=instance.owner,
                      owner_rev_post=instance,
                      title_post_rev=instance.title,
                      description_post_rev=instance.description,
                      link_rev=instance.link,
                      photo_rev=instance.photo)


# Create ghnRevPost after saving a new pcsa_GHN post
post_save.connect(create_revpost, sender=ghnPost)

# Create a ghnRevPost after updating an already existing pcsa_GHN post
post_update.connect(create_revpost, sender=ghnPost)
