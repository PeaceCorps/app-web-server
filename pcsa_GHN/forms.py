from django.forms import ModelForm

from pcsa_GHN.models import Contact, ghnPost


class ghnPostForm(ModelForm):
    class Meta:
        model = ghnPost
        fields = ['title', 'description','link','photo']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['office_name', 'contact_number']
