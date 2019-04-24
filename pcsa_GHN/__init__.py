from django.forms.fields import CharField, IntegerField


"""Set app configuration by calling function"""

default_app_config = "pcsa_GHN.apps.PCSA_GHNConfig"

"""
Helper method so that user cannot enter a white space to save data anywhere
"""

def new_clean(self, value):
	"""
	Strip leading and traling whitespaces on all the CharField values
	"""
	if value:
		try:
			value = value.strip()
		except:
			pass
			
	return super(CharField, self).clean(value)
	
CharField.clean = new_clean


def new_clean_number(self, value):
	"""
	This function lets the user enter any number only for the BigInteger
	If the number starts from any whitespace by accident, it strips it away.
	"""
	if value:
		try:
			value = value.strip()
		except:
			pass
		
		return super(IntegerField, self).clean(value)
		
IntegerField.clean = new_clean_number
