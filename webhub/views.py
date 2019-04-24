
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, viewsets

from rest_framework.decorators import api_view

from django.shortcuts import render, redirect

from webhub.serializers import *
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from profiles.models import Pcuser
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from webhub import views as webhub_view
from malaria_web.models import Post
from pcsa_GHN.models import ghnPost
from pcsa_safety_tools.models import SafetyToolsPost
from itertools import chain


# SMTP port for sending emails
SMTP_PORT = 465

# Link for the localhost
website = "http://systerspcweb.herokuapp.com/"

# APIs for malaria begin here
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ListUsers(APIView):

    def get(self, request, format=None):
        pcuser = Pcuser.objects.all()
        serializer = PcuserSerializer(pcuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PcuserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PcuserDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Pcuser.objects.get(pk=pk)
        except Pcuser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PcuserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PcuserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Display the main page of the project with malaria and pcsa app options
class DashboardView(LoginRequiredMixin,TemplateView):

    template_name = 'ui/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


# Information about PeaceCorps in the footer section
class AboutPC(TemplateView):
    
    template_name = 'ui/aboutPC.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPC, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


# PeaceCorps policies in the footer section
class Policies(TemplateView):
    
    template_name = 'ui/policies.html'

    def get_context_data(self, **kwargs):
        context = super(Policies, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


# PeaceCorps details in the footer section
class Details(TemplateView):
    
    template_name = 'ui/details.html'

    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


# PeaceCorps help in the footer section
class HelpPC(TemplateView):
    
    template_name = 'ui/helpPC.html'

    def get_context_data(self, **kwargs):
        context = super(HelpPC, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


# Search through posts (displayed on the right corner of the dashboard)
class PostSearchView(ListView):

    template_name = 'ui/result.html'
    model = Post

    def get_queryset(self):
        
        result = super(PostSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        category = self.request.GET.get('category')
        
        if query:
            if category == 'firstaide':
                result = ghnPost.objects.filter(title__icontains=query)
            elif category == 'firstaide_safety_tools':
                result = SafetyToolsPost.objects.filter(title__icontains=query)
            elif category == 'malaria':
                result = Post.objects.filter(title_post__icontains=query)
            else:
                result = list(chain(Post.objects.filter(title_post__icontains=query),
                            ghnPost.objects.filter(title__icontains=query),
                            SafetyToolsPost.objects.filter(title__icontains=query)))
        return result

    def get_context_data(self, **kwargs):

        context = super(PostSearchView, self).get_context_data(*kwargs)
        category = self.request.GET.get('category')
        context['category'] = category
        return context


class LoginReal(TemplateView):
    template_name="login_real.html"


def login_social(request):
    username= request.POST['uname']
    user=User.objects.get(username=username)
    print(user.email)
    print(username)
    gender="Restricted"
    location= "N.A"
    phone="N.A"
    num_results = Pcuser.objects.filter(user=user).count()
    if num_results ==0:
           
        print("num rsults")
        print(num_results)
    
        entry = Pcuser(user=user, phone=phone, gender=gender, location=location, verified = uuid.uuid4().hex)      
        entry.save()
    else:
        print("num rsults")
        print(num_results)
        pcuser=Pcuser.objects.get(user=user)
        entry=pcuser

    # if 'redirect' in request.POST.keys():
    #     return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":request.POST['redirect'].replace("!!__!!","&")}))
    # return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":"/"}))
    return redirect("dashboard")

