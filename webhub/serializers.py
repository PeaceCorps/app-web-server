from django.contrib.auth.models import User
from signup.models import *

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email','id')

class PcuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcuser
        fields = ('user', 'location', 'phone', 'gender','id')