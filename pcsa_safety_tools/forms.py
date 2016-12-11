from django.forms import ModelForm
from .models import SafetyToolsPost


class SafetyToolsPostForm(ModelForm):
    class Meta:
        model = SafetyToolsPost
        fields = ['category_id','title', 'description']