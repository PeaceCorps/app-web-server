from django.db import models
from django.core.validators import RegexValidator
from signup.models import Pcuser


class Post(models.Model):
    # The owner of the post
    owner = models.ForeignKey(Pcuser, null=False, related_name='owner')
    title_post = models.CharField(max_length=1000,
                                  validators=[
                                      RegexValidator(
                                          r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                      )]
                                  )
    description_post = models.TextField(max_length=20000,
                                        validators=[
                                            RegexValidator(
                                                r'^[(A-Z)|(a-z)|(0-9)|(\n)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)|(\')]+$'
                                            )]
                                        )
    # link to important documents
    link_post = models.CharField(max_length=2000)
    # field to note the timestamp when the post was created
    created = models.DateTimeField(auto_now_add=True)
    # field to note the timestamp when the post was last updated
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.owner.user.username


class RevPost(models.Model):
    # The post which is being edited
    owner_rev_post = models.ForeignKey(Post,
                                       null=False,
                                       related_name='owner_rev_post')
    # The user who is editing the post
    owner_rev = models.ForeignKey(Pcuser, null=False, related_name='owner_rev')
    # revised title
    title_post_rev = models.CharField(max_length=1000,
                                      validators=[
                                          RegexValidator(
                                              r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                          )]
                                      )
    # revised description
    description_post_rev = models.TextField(max_length=20000,
                                            validators=[
                                                RegexValidator(
                                                    r'^[(A-Z)|(a-z)|(0-9)|(\n)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                                )]
                                            )
    # field to note the timestamp when the revised version was created
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.owner_rev.user.username


class MalariaUsers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    medicineType = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
