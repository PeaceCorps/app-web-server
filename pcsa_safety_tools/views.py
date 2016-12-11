from django.shortcuts import render
from .models import SafetyToolsPost
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from .services import *
from .forms import SafetyToolsPostForm
from django.core.urlresolvers import reverse
from .serializers import SafetyToolsPostSerializer
from rest_framework import viewsets


# Create your views here.

class SafetyToolsPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SafetyToolsPost.objects.all()
    serializer_class = SafetyToolsPostSerializer


post_list = SafetyToolsPost.objects.all()


def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))
    radar = SafetyToolsPost.objects.filter(category_id=1)
    unwanted_attention = SafetyToolsPost.objects.filter(category_id=2)
    tactics = SafetyToolsPost.objects.filter(category_id=3)
    bystander_intervention = SafetyToolsPost.objects.filter(category_id=4)
    safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5)
    safety_plan = SafetyToolsPost.objects.filter(category_id=6)
    categories = [radar, unwanted_attention, tactics, bystander_intervention, safety_plan_basics, safety_plan]

    return render(request, 'pcsa_safety_tools/home.html', {'categories': categories})


def create_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = SafetyToolsPostForm()
    if request.method == 'POST':
        form = SafetyToolsPostForm(request.POST)
        if form.is_valid():
            post = create_post_from_form(form)
            return render(request,
                          'pcsa_safety_tools/view_post.html',
                          {'post': post})

    return render(request,
                  'pcsa_safety_tools/create_post.html',
                  {'form': form})



def edit_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        if request.method == 'POST':

            # need to get the original title_post and description_post
            # before it is changed when calling instance on PostForm
            orig_title = post.title
            orig_desc = post.description
            form = SafetyToolsPostForm(request.POST, instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title']
                edited_desc = form.cleaned_data['description']

                if (orig_title != edited_title) or \
                        (orig_desc != edited_desc):
                    post = create_post_from_form(form, owner)

                return HttpResponseRedirect(reverse('pcsa_safety_tools:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'pcsa_safety_tools/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = SafetyToolsPostForm(instance=post)
            return render(request,
                          'pcsa_safety_tools/edit_post.html',
                          {'form': form, 'post': post})
    else:
        raise Http404


def delete_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if delete_post_by_id(post_id):
            return HttpResponseRedirect(reverse('pcsa_safety_tools:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_safety_tools/delete_post.html',
                      {'post_id': post_id})


def view_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        return render(request,
                      'pcsa_safety_tools/view_post.html',
                      {'post': post})
    else:
        raise Http404
