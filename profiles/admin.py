from django.contrib import admin
from django.contrib.auth import admin as upstream
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Pcuser

class EmailRequiredMixin(object):
	def __init__(self, *args, **kwargs):
		super(EmailRequiredMixin, self).__init__(*args, **kwargs)
		# Make the email field mandatory
		self.fields['email'].required = True

class FirstNameRequiredMixin(object):
	def __init__(self, *args, **kwargs):
		super(FirstNameRequiredMixin, self).__init__(*args, **kwargs)
		# Make the first name mandatory
		self.fields['first_name'].required = True
		
class LastNameRequiredMixin(object):
	def __init__(self, *args, **kwargs):
		super(LastNameRequiredMixin, self).__init__(*args, **kwargs)
		# Make the last name mandatory
		self.fields['last_name'].required = True
		
class MyUserCreationForm(EmailRequiredMixin, FirstNameRequiredMixin, LastNameRequiredMixin, UserCreationForm):
	pass
	
class MyUserChangeForm(EmailRequiredMixin, FirstNameRequiredMixin, LastNameRequiredMixin, UserChangeForm):
	pass
	
class EmailRequiredUserAdmin(UserAdmin):
	form = MyUserChangeForm
	add_form = MyUserCreationForm
	add_fieldsets = ((None, {'fields': ('username', 'email', 'first_name', 'last_name',
						'password1', 'password2'), 'classes' : ('wide',)}),)

# Registering the models						
admin.site.unregister(User)
admin.site.register(User, EmailRequiredUserAdmin)
admin.site.register(Pcuser)