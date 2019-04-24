from django.shortcuts import render

from .forms import *
from .models import *
from rest_framework import viewsets
from django.http import *
from .serializers import *
from rest_framework.response import Response
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# View to render the JSON
class FirstAideAPIViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = firstAideAPISerializer
    page_id=""
    page_type=""
    title=""

    # When you set queryset (model = xyz), the queryset is created only once, when you start your server.
    # On the other hand, the get_queryset method is called for every request.
    def get_queryset(self):
        # Get all model instances with a particular 'id'
        queryset = FirstAideAPI.objects.all().filter(post_id=self.kwargs['id'])
        # Get the page_id of the first instance (all instances with a particular id will have the same value for this field)
        FirstAideAPIViewSet.page_id = queryset.values_list('post_id',flat=True)[0]
        # Get the page_type of the first instance (all instances with a particular id will have the same value for this field)
        FirstAideAPIViewSet.page_type = queryset.values_list('page_type',flat=True)[0]
        # Get the title of the first instance (all instances with a particular id will have the same value for this field)
        FirstAideAPIViewSet.title= queryset.values_list('title',flat=True)[0]
        return queryset

    def list(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(instance, many=True)

        # Create the JSON to be rendered
        serializer_data = {"page_id": FirstAideAPIViewSet.page_id,"page_type":FirstAideAPIViewSet.page_type,"title":FirstAideAPIViewSet.title}
        # Append the JSON with the card content
        serializer_data .update({"content": {"cards":serializer.data}})
        return Response(serializer_data) 

#View to list the cards
class ListFirstAideAPIView(LoginRequiredMixin, ListView):

    model = FirstAideAPI

    # HTML Template rendering the form
    template_name = 'firstaide/home.html'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListFirstAideAPIView, self).get_context_data(**kwargs)
        # Get model instances sorted by their post_ids
        context['post_list'] = FirstAideAPI.objects.all().order_by('post_id')
        return context

# View to add a card
class CreateFirstAideAPIView(LoginRequiredMixin, CreateView):
    
    model = FirstAideAPI
    form_class = FirstAideAPIForm
    # HTML Template rendering the form
    template_name = 'firstaide/create_post.html'
    # URL to be visited after successfully creating a model instance
    success_url='/firstaide/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreateFirstAideAPIView, self).form_valid(form)

# View to edit a card
class UpdateFirstAideAPIView(LoginRequiredMixin, UpdateView):
    
    model = FirstAideAPI
    form_class = FirstAideAPIForm
    # HTML Template rendering the form
    template_name = "firstaide/edit_post.html"
    # URL to be visited after successfully updating a model instance
    success_url='/firstaide/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdateFirstAideAPIView, self).form_valid(form)


# View to delete a card
class DeleteFirstAideAPIView(LoginRequiredMixin, DeleteView):

    model = FirstAideAPI
    # HTML Template rendering the form
    template_name = "firstaide/delete_post.html"
    # URL to be visited after successfully deleting a model instance
    success_url = '/firstaide/'
    redirect_field_name = 'redirect_to'


# View to view a single card
class ViewFirstAideAPIView(LoginRequiredMixin, DetailView):
    model = FirstAideAPI
    # HTML Template rendering the form
    template_name = "firstaide/view_post.html"
    redirect_field_name = 'redirect_to'
