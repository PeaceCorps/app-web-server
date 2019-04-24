from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .forms import ContactForm, ghnPostForm
from .models import Contact, ghnPost, ghnRevPost
from .serializers import ContactSerializer, ghnPostSerializer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ghnPostsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ghnPost.objects.all()
    serializer_class = ghnPostSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Main page to display list of all pcsa get help now posts and contacts
class ListPostView(LoginRequiredMixin, ListView):

    model = ghnPost
    template_name = 'pcsa_GHN/home.html'
    redirect_field_name = 'redirect_to'

    # For sorting contacts
    def get_context_data(self, **kwargs):
        context = super(ListPostView, self).get_context_data(**kwargs)
        context['contact_list'] = Contact.objects.all()
        category_contact = self.request.GET.get('category_contact')
        if category_contact:
            if self.request.GET:
                if self.request.GET.get('asc'):
                    context['contact_list'] = Contact.objects.order_by(category_contact)
                elif self.request.GET.get('desc'):
                    context['contact_list'] = Contact.objects.order_by('-'+category_contact)
        return context

    # For sorting posts
    def get_queryset(self):
        result = super(ListPostView, self).get_queryset()
        category = self.request.GET.get('category')
        if category:
            if self.request.GET:
                if self.request.GET.get('asc'):
                    result = ghnPost.objects.order_by(category)
                elif self.request.GET.get('desc'):
                   result = ghnPost.objects.order_by('-'+category)
        return result


# To create a new pcsa post
class CreatePostView(LoginRequiredMixin, CreateView):
    
    model = ghnPost
    form_class = ghnPostForm
    template_name = 'pcsa_GHN/create_post.html'
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)


# To edit an already created post
class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = ghnPost
    form_class = ghnPostForm
    template_name = "pcsa_GHN/edit_post.html"
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


# To delete a post
class DeletePostView(LoginRequiredMixin, DeleteView):

    model = ghnPost
    success_url = '/gethelpnow/'
    redirect_field_name = 'redirect_to'


# To view the details of a post
class ViewPostView(LoginRequiredMixin, DetailView):
    model = ghnPost
    template_name = "pcsa_GHN/view_post.html"
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ViewPostView, self).get_context_data(**kwargs)
        revpost_list = ghnRevPost.objects.filter(owner_rev_post_id=self.kwargs['pk'])
        context['revpost_list'] = revpost_list
        return context


# To create a new pcsa contact
class CreateContactView(LoginRequiredMixin, CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'pcsa_GHN/create_contact.html'
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreateContactView, self).form_valid(form)


# To edit an already created contact
class UpdateContactView(LoginRequiredMixin, UpdateView):
    
    model = Contact
    form_class = ContactForm
    template_name = "pcsa_GHN/edit_contact.html"
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdateContactView, self).form_valid(form)


# To delete a contact
class DeleteContactView(LoginRequiredMixin, DeleteView):

    model = Contact
    template_name = "pcsa_GHN/delete_contact.html"
    success_url = '/gethelpnow/'
    redirect_field_name = 'redirect_to'


# To view the details of a contact
class ViewContactView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "pcsa_GHN/view_contact.html"
    redirect_field_name = 'redirect_to'
