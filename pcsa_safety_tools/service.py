from django.core.exceptions import ObjectDoesNotExist

from .models import SafetyToolsCategory, SafetyToolsPost


def create_post_from_form(form):

    post = None
    if form :
        post = form.save(commit=False)
        post.save()
    return post


def delete_post_by_id(post_id):

    is_deleted = False
    try:
        post = SafetyToolsPost.objects.get(pk=post_id)
        post.delete()
        is_deleted = True
    except ObjectDoesNotExist:
        pass

    return is_deleted


def get_post_by_id(post_id):

    post = None
    try:
        post = SafetyToolsPost.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        pass

    return post