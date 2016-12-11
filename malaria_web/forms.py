from django.forms import ModelForm
from malaria_web.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title_post', 'description_post']
