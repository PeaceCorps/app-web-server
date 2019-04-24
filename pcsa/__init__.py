from django.forms.fields import CharField

"""Set app configuration by calling function"""
default_app_config = 'pcsa.apps.PCSAConfig'

def new_clean(self, value):
	"""
	Strip leading and trailing whitespaces on all CharFields
	"""
	if value:
		# we try/catch here, because other field subclass CharField
		try:
			value = value.strip()
		except:
			pass
			
	return super(CharField, self).clean(value)
	
CharField.clean = new_clean
