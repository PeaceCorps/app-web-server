from rest_framework import serializers
from .models import PcsaPost


class PcsaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcsaPost
        fields = ('owner',
                  'title',
                  'description',
                  'created',
                  'id')
