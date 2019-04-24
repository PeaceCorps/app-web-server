from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from pcsa.forms import PostForm
from pcsa.models import PcsaPost
from .models import PcsaPost
from .serializers import PcsaPostSerializer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class PcsaPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post endpoint that provides `list` and `detail` actions
    `list` action returns a list of all Posts
    `detail` action returns a particular Post instance based on id
    """
    queryset = PcsaPost.objects.all()
    serializer_class = PcsaPostSerializer


class ListPostView(ListView):

    model = PcsaPost
    template_name = 'pcsa/list_posts.html'


class CreatePostView(LoginRequiredMixin, CreateView):

    model = PcsaPost
    form_class = PostForm
    template_name = 'pcsa/create_post.html'
    success_url='/pcsa/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = PcsaPost
    fields = ['title','description']
    template_name = "pcsa/edit_post.html"
    success_url='/pcsa/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = PcsaPost
    template_name = "pcsa/delete_post.html"
    success_url = '/pcsa/list_posts'
    redirect_field_name = 'redirect_to'


class ViewPostView(LoginRequiredMixin, DetailView):

    model = PcsaPost
    template_name = "pcsa/view_post.html"
    redirect_field_name = 'redirect_to'