from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
import urllib.request, json 

from malaria_web.forms import PostForm
from malaria_web.models import Post, RevPost, MalariaUsers
from malaria_web.services import (create_post_from_form, create_revpost,
                                  delete_post_by_id, get_post_by_id,
                                  get_revposts_of_owner)

from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# View to list all the Malaria Posts
class ListPostView(LoginRequiredMixin, ListView):

    model = Post
    # HTML Template rendering the form
    template_name = 'malaria/list_posts.html'
    redirect_field_name = 'redirect_to'

    ''' 
      When you set queryset (model = xyz), the queryset is created only once, when you start your server
      but the get_queryset method is called for every request
    '''
    def get_queryset(self):
        result = super(ListPostView, self).get_queryset()
        category = self.request.GET.get('category')
        if category:
            if self.request.GET:
                if self.request.GET.get('asc'):
                    result = Post.objects.order_by(category)
                elif self.request.GET.get('desc'):
                   result = Post.objects.order_by('-'+category)
                print(result)

        return result


# View to Create a new malaria post
class CreatePostView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = PostForm
    template_name = 'malaria/create_post.html'
    success_url='/malaria/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)



# View to Edit an already created post
class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = Post
    form_class = PostForm
    template_name = "malaria/edit_post.html"
    success_url='/malaria/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


# View to Delete a post
class DeletePostView(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = '/malaria/list_posts'
    redirect_field_name = 'redirect_to'

# View to get Details of a post
class ViewPostView(LoginRequiredMixin, DetailView):

    model = Post
    template_name = "malaria/view_post.html"
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ViewPostView, self).get_context_data(**kwargs)
        revpost_list = RevPost.objects.filter(owner_rev_post_id=self.kwargs['pk'])
        context['revpost_list'] = revpost_list
        return context

#  View to get JSON from web and convert it to python objects
class ListAppUsersView(LoginRequiredMixin, ListView):
    ''' 
      When you set queryset (model = xyz), the queryset is created only once, when you start your server
      but the get_queryset method is called for every request
    '''
    def get_queryset(self):
        with urllib.request.urlopen("https://rawgit.com/yatna/0e6b1ce2435de3e10a779aad40b4375b/raw/Malaria_users.json") as url:
            data = json.loads(url.read().decode())
            '''
            data is of type - List of dictionaries 
            Eg: [
              {
                name:'yatna',
                email:'yatnavermaa@gmail.com',
                age=21,
                gender='Male',
                medicineType='Malrone'
               },
              {
                name:'annie', 
                email:'shmulders@gmail.com', 
                age=21, gender='female', 
                medicineType='Mefloquine'
                }
              ]
            '''
            for user in data:
                # Creates an instance of model only if similar data does not exist, else gets the previous one
                MalariaUsers.objects.get_or_create(name=user['name'],email=user['email'],age=user['age'],gender=user['gender'],medicineType=user['medicineType'])
        queryset = MalariaUsers.objects.all()
        return queryset

    template_name = 'malaria/list_app_users.html'
    redirect_field_name = 'redirect_to'
