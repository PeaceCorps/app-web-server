from profiles.models import Pcuser
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PcuserForm
from allauth.account.views import PasswordChangeView


# View the profile of the user
class ProfileView(LoginRequiredMixin, TemplateView):

    # HTML Template rendering the form
    template_name = 'profiles/profile.html'

    # Pass the information required to display the profile view template
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['pcuser'] = self.request.user.pcuser
        return context


# Edit profile
class EditProfile(LoginRequiredMixin, UpdateView):
    
    # HTML Template rendering the form
    template_name = 'profiles/edit_profile.html'
    form_class = PcuserForm
    model = Pcuser
    success_url = "/profile/"


    # Save the edited form
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user.username = self.request.POST['username']
        instance.user.first_name = self.request.POST['first_name']
        instance.user.last_name = self.request.POST['last_name']
        instance.user.email = self.request.POST['email']
        instance.user.save()
        return super(EditProfile, self).form_valid(form)
