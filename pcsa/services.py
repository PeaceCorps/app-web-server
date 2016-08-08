from django.core.exceptions import ObjectDoesNotExist
from pcsa.models import PcsaPost


def create_post_from_form(form, owner):

    post = None
    if form and owner:
        post = form.save(commit=False)
        post.owner = owner
        post.save()
    return post


def delete_post_by_id(post_id):

    is_deleted = False
    try:
        post = PcsaPost.objects.get(pk=post_id)
        post.delete()
        is_deleted = True
    except ObjectDoesNotExist:
        pass

    return is_deleted


def get_post_by_id(post_id):

    post = None
    try:
        post = PcsaPost.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        pass

    return post
