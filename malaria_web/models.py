from django.core.validators import RegexValidator
from django.db import models
from django.core.files.storage import FileSystemStorage

from profiles.models import Pcuser
from django.db.models.signals import post_save
from django.dispatch import Signal

post_update = Signal()

# Model corresponding to malaria posts
class Post(models.Model):
    # Owner of the post
    owner = models.ForeignKey(Pcuser, null=False, related_name='owner')
    title_post = models.CharField(max_length=1000,
                                  validators=[
                                      RegexValidator(
                                          r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                      )]
                                  )
    description_post = models.TextField(max_length=20000)
    # Link to important documents
    link_post = models.CharField(max_length=200)

    # Define where the images in posts will be stored
    fs = FileSystemStorage(location='static/')
    # uploadable image in posts
    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    # Timestamp recorded when new Post created
    created = models.DateTimeField(auto_now_add=True)
    # Field to note the timestamp when the post was last updated
    updated = models.DateTimeField(auto_now=True)

    # Name to be shown for a particular instance of this type of model
    def __str__(self):
        return self.owner.user.username

    # To get url of model in templates
    def get_absolute_url(self):
        return '/malaria/view_post/%i' % self.id

    # To access the model name in templates
    def model_name(self):
        return 'Malaria'
    
    # Name to be shown on the home page of the admin view for the collective set of model instances
    class Meta:
    	verbose_name = 'Post'
    	verbose_name_plural = 'Posts'


# Model corresponding to Revision History of Malaria Posts
class RevPost(models.Model):
    # The post which is being edited
    owner_rev_post = models.ForeignKey(Post,
                                       null=False,
                                       related_name='owner_rev_post')
    # User who is editing the post
    owner_rev = models.ForeignKey(Pcuser, null=False, related_name='owner_rev')
    # Revised title
    title_post_rev = models.CharField(max_length=1000)
    # Revised description
    description_post_rev = models.TextField(max_length=20000,
                                            validators=[
                                                RegexValidator(
                                                    r'^[(A-Z)|(a-z)|(0-9)|(\n)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                                )]
                                            )


    # Timestamp recorded when the Post is submitted for edit
    created = models.DateTimeField(auto_now_add=True)

    link_rev = models.CharField(max_length=200)

    fs = FileSystemStorage(location='static/')

    photo_rev = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    def __str__(self):
        return self.owner_rev.user.username
        
    class Meta:
    	verbose_name = 'Reviewed Post'
    	verbose_name_plural = 'Reviewed Posts'


# Signal to RevPost when a new post is created or updated
def create_revpost(sender, instance, created, **kwargs):
    RevPost.objects.create(owner_rev=instance.owner,
                      owner_rev_post=instance,
                      title_post_rev=instance.title_post,
                      description_post_rev=instance.description_post,
                      link_rev=instance.link_post,
                      photo_rev=instance.photo)


# Create RevPost after saving a new malaria post
post_save.connect(create_revpost, sender=Post)

# Create a RevPost after updating an already existing malaria post
post_update.connect(create_revpost, sender=Post)


# Model to store Malaria Users
class MalariaUsers(models.Model):
    # Name of the user
    name = models.CharField(max_length=200)
    # Email of the user
    email = models.EmailField(max_length=254)
    # Age of the user
    age = models.IntegerField()
    # Gender of the user
    gender = models.CharField(max_length=20, default='Not Specified')
    # Medicine he/she is taking eg Mefloquine, Malarone etc
    medicineType = models.CharField(max_length=100)

    # Name to be shown for a particular instance of this type of model
    def __str__(self):
        return self.name

    # Name to be shown on the home page of the admin view for the collective set of model instances
    class Meta:
        verbose_name = 'Malaria App Users'
