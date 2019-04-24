from rest_framework import serializers

from .models import *


class firstAideAPISerializer(serializers.ModelSerializer):
    # Serializers convert python objects to serialized form such as JSON or text
    class Meta:
        model = FirstAideAPI
        # List of fields in above model to be serialized
        fields = ('card_content',)
