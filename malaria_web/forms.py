from django.forms import ModelForm

from malaria_web.models import Post

# Forms convert model fields to HTML fields
class PostForm(ModelForm):
    class Meta:
        model = Post
        # List of fields to be available in HTML
        fields = ['title_post', 'description_post','link_post','photo']
