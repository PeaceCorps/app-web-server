from django.forms import ModelForm
from pcsa.models import PcsaPost


class PostForm(ModelForm):
    class Meta:
        model = PcsaPost
        fields = ['title', 'description']
