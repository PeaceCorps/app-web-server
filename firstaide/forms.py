from django.forms import ModelForm
from firstaide.models import *

class FirstAideAPIForm(ModelForm):
	# Forms convert model fields to HTML fields
	class Meta:
		model = FirstAideAPI
		# List of fields to be available in HTML
		fields = ['post_id','page_type','title','card_content']

