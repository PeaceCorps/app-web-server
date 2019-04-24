from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .forms import SafetyToolsPostForm
from .models import SafetyToolsPost, safetyRevPost
from .serializers import SafetyToolsPostSerializer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class SafetyToolsPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SafetyToolsPost.objects.all()
    serializer_class = SafetyToolsPostSerializer


# Main page to display list of all pcsa safety tools posts separated as per category
class ListPostView(LoginRequiredMixin, ListView):

    model = SafetyToolsPost
    template_name = 'pcsa_safety_tools/home.html'

    def get_context_data(self, **kwargs):
        radar = SafetyToolsPost.objects.filter(category_id=1)
        unwanted_attention = SafetyToolsPost.objects.filter(category_id=2)
        tactics = SafetyToolsPost.objects.filter(category_id=3)
        bystander_intervention = SafetyToolsPost.objects.filter(category_id=4)
        safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5)
        safety_plan = SafetyToolsPost.objects.filter(category_id=6)
        category = self.request.GET.get('category')
        # For sorting
        if category:
            if self.request.GET:
                if self.request.GET.get('asc'):
                    radar = SafetyToolsPost.objects.filter(category_id=1).order_by(category)
                    unwanted_attention = SafetyToolsPost.objects.filter(category_id=2).order_by(category)
                    tactics = SafetyToolsPost.objects.filter(category_id=3).order_by(category)
                    bystander_intervention = SafetyToolsPost.objects.filter(category_id=4).order_by(category)
                    safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5).order_by(category)
                    safety_plan = SafetyToolsPost.objects.filter(category_id=6).order_by(category)
                elif self.request.GET.get('desc'):
                    radar = SafetyToolsPost.objects.filter(category_id=1).order_by('-'+category)
                    unwanted_attention = SafetyToolsPost.objects.filter(category_id=2).order_by('-'+category)
                    tactics = SafetyToolsPost.objects.filter(category_id=3).order_by('-'+category)
                    bystander_intervention = SafetyToolsPost.objects.filter(category_id=4).order_by('-'+category)
                    safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5).order_by('-'+category)
                    safety_plan = SafetyToolsPost.objects.filter(category_id=6).order_by('-'+category)
        categories = [radar, unwanted_attention, tactics, bystander_intervention, safety_plan_basics, safety_plan]
        context = super(ListPostView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context

    def get_queryset(self):
        result = super(ListPostView, self).get_queryset()
        return result


# To create a new pcsa safety tools post
class CreatePostView(LoginRequiredMixin, CreateView):
    
    model = SafetyToolsPost
    form_class = SafetyToolsPostForm
    template_name = 'pcsa_safety_tools/create_post.html'
    success_url='/safetytools/home/'


# To edit an already created post
class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = SafetyToolsPost
    form_class= SafetyToolsPostForm
    template_name = "pcsa_safety_tools/edit_post.html"
    success_url='/safetytools/home/'


# To delete a post
class DeletePostView(LoginRequiredMixin, DeleteView):

    model = SafetyToolsPost
    template_name = "pcsa_safety_tools/delete_post.html"
    success_url = '/safetytools/home/'


# To view the details of a post
class ViewPostView(LoginRequiredMixin, DetailView):
    model = SafetyToolsPost
    template_name = "pcsa_safety_tools/view_post.html"

    def get_context_data(self, **kwargs):
        context = super(ViewPostView, self).get_context_data(**kwargs)
        revpost_list = safetyRevPost.objects.filter(owner_rev_post_id=self.kwargs['pk'])
        context['revpost_list'] = revpost_list
        return context
