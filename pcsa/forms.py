from django.forms import ModelForm
from django import forms

from pcsa.models import PcsaPost

class StripTextField(forms.CharField):
	
	def clean(self, value):
		return value.strip()


class StripWhitespaceMixin(object):
	
	def _clean_fields(self):
		"""
		value_from_datadict() gets the data from the data dict.
		Each widget type knows how to retrieve its own data, because
		some fields split data over several HTML fields
		"""
		value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
		
		try:
			if isinstance(field, CharField):
				initial = self.initial.get(name, field.initial)
				value = field.clean(value, initial)
			else:
				if isinstance(value, basestring):
					value = field.clean(value.strip())
				else:
					value = field.clean(value)
			self.cleaned_data[name] = value
			if hasattr(self, 'clean_%s' % name):
				value = getattr(self, 'clean_%s' % name)()
				self.cleaned_data[name] = value
				
		except ValidationError as e:
			self._errors[name] = self.error_class(e.messages)
			if name is self.cleaned_data:
				del self.cleaned_data[name]


class PostForm(StripTextField, ModelForm):

    strip_field = StripTextField()
	
    class Meta:
        model = PcsaPost
        fields = ['title', 'description']
