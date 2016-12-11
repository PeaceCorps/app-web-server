from django.shortcuts import render
from .models import Contact, ghnPost
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from .services import *
from .forms import ghnPostForm, ContactForm
from django.core.urlresolvers import reverse
from .serializers import ghnPostSerializer, ContactSerializer
from rest_framework import viewsets

# Create your views here.

class ghnPostsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ghnPost.objects.all()
    serializer_class = ghnPostSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

post_list = ghnPost.objects.all()
contact_list = Contact.objects.all()


def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))
    post_list = ghnPost.objects.all()
    contact_list = Contact.objects.all()
    return render(request, 'pcsa_GHN/home.html', {'post_list': post_list, 'contact_list': contact_list})


def create_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = ghnPostForm()
    if request.method == 'POST':
        form = ghnPostForm(request.POST)
        if form.is_valid():
            owner = request.user.pcuser
            post = create_post_from_form(form, owner)
            return render(request,
                          'pcsa_GHN/view_post.html',
                          {'post': post})

    return render(request,
                  'pcsa_GHN/create_post.html',
                  {'form': form})


def create_contact(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return render(request,
                          'pcsa_GHN/view_contact.html',
                          {'contact':contact})

    return render(request,
                  'pcsa_GHN/create_contact.html',
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
            form = ghnPostForm(request.POST, instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title']
                edited_desc = form.cleaned_data['description']

                if (orig_title != edited_title) or \
                        (orig_desc != edited_desc):
                    post = create_post_from_form(form, owner)

                return HttpResponseRedirect(reverse('pcsa_GHN:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'pcsa_GHN/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = ghnPostForm(instance=post)
            return render(request,
                          'pcsa_GHN/edit_post.html',
                          {'form': form, 'post': post})
    else:
        raise Http404


def edit_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    contact = Contact.objects.get(pk=contact_id)
    if contact:
        if request.method == 'POST':

            # need to get the original title_post and description_post
            # before it is changed when calling instance on PostForm
            orig_title = contact.title
            orig_desc = contact.description
            form = ContactForm(request.POST, instance=contact)

            if form.is_valid():

                edited_name = form.cleaned_data['office_name']
                edited_number = form.cleaned_data['contact_number']

                if (orig_title != edited_name) or \
                        (orig_desc != edited_number):
                    form.save()

                return render(request,
                              'pcsa_GHN/home.html',
                              {'post_list': post_list, 'contact_list': contact_list})
            else:
                return render(request,
                              'pcsa_GHN/edit_contact.html',
                              {'form': form, 'contact': contact})
        else:
            form = ghnPostForm(instance=contact)
            return render(request,
                          'pcsa_GHN/edit_contact.html',
                          {'form': form, 'contact': contact})
    else:
        raise Http404


def delete_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if delete_post_by_id(post_id):
            return HttpResponseRedirect(reverse('pcsa_GHN:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_GHN/delete_post.html',
                      {'post_id': post_id})


def delete_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if contact_id:
            contact = Contact.objects.get(pk=contact_id)
            contact.delete()
            return HttpResponseRedirect(reverse('pcsa_GHN:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_GHN/delete_contact.html',
                      {'contact_id': contact_id})


def view_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        return render(request,
                      'pcsa_GHN/view_post.html',
                      {'post': post})
    else:
        raise Http404

def view_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    contact = Contact.objects.get(pk = contact_id)
    if contact:
        return render(request,
                      'pcsa_GHN/view_post.html',
                      {'contact': contact})
    else:
        raise Http404
