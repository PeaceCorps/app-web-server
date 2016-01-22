from django.core.exceptions import ObjectDoesNotExist
from malaria.models import Post, RevPost


def create_post_from_form(form, owner):

    post = None

    if form and owner:
        post = form.save(commit=False)
        post.owner = owner
        post.save()

    return post


def create_revpost(owner, post, title, description):

    revpost = None

    if owner and post and title and description:
        # title_change and description_change fields
        # are not being used, may have to remove from model later
        revpost = RevPost(owner_rev=owner,
                          owner_rev_post=post,
                          title_post_rev=title,
                          description_post_rev=description,
                          title_change=True)
        revpost.save()

    return revpost


def delete_post_by_id(post_id):

    is_deleted = False
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
        is_deleted = True
    except ObjectDoesNotExist:
        pass

    return is_deleted


def get_post_by_id(post_id):

    post = None
    try:
        post = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        pass

    return post


def get_revposts_of_owner(post_id):

    revpost_list = None
    try:
        revpost_list = RevPost.objects.filter(owner_rev_post_id=post_id)
    except ObjectDoesNotExist:
        pass

    return revpost_list
