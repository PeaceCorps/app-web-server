from rest_framework import serializers

from .models import *


class SafetyToolsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyToolsPost
        fields = ('category_id','title', 'description', 'created_date')
