from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from malaria.forms import PostForm
from malaria.models import Post
from malaria.services import create_post_from_form, create_revpost, \
    delete_post_by_id, get_post_by_id, get_revposts_of_owner


def list_posts(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post_list = Post.objects.all()
    return render(request,
                  'malaria/list_posts.html',
                  {'post_list': post_list})


def create_post(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title_post']
            description = form.cleaned_data['description_post']
            owner = request.user.pcuser
            post = create_post_from_form(form, owner)

            if post:
                revpost = create_revpost(owner, post, title, description)
                if revpost:
                    return HttpResponseRedirect(reverse('malaria:list_posts'))
                else:
                    raise Http404
            else:
                raise Http404

    return render(request,
                  'malaria/create_post.html',
                  {'form': form})


def edit_post(request, post_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        if request.method == 'POST':

            # need to get the original title_post and description_post
            # before it is changed when calling instance on PostForm
            orig_title = post.title_post
            orig_desc = post.description_post
            form = PostForm(request.POST, instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title_post']
                edited_desc = form.cleaned_data['description_post']

                if (orig_title != edited_title) or \
                   (orig_desc != edited_desc):

                    post = create_post_from_form(form, owner)

                    if post:
                        revpost = create_revpost(owner,
                                                 post,
                                                 edited_title,
                                                 edited_desc)
                        if not revpost:
                            raise Http404
                    else:
                        raise Http404

                return HttpResponseRedirect(reverse('malaria:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'malaria/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = PostForm(instance=post)
            return render(request,
                          'malaria/edit_post.html',
                          {'form': form, 'post': post})
    else:
        raise Http404


def delete_post(request, post_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if delete_post_by_id(post_id):
            return HttpResponseRedirect(reverse('malaria:list_posts'))
        else:
            raise Http404
    else:
        return render(request,
                      'malaria/delete_post.html',
                      {'post_id': post_id})


def view_post(request, post_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    revpost_list = get_revposts_of_owner(post_id)
    # revpost may not exist yet so do not check it
    if post:
        return render(request,
                      'malaria/view_post.html',
                      {'post': post,
                       'revpost_list': revpost_list})
    else:
        raise Http404
