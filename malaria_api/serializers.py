from rest_framework import serializers
from malaria_web.models import Post, MalariaUsers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('owner',
                  'title_post',
                  'description_post',
                  'created',
                  'updated',
                  'id')
class MalariaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalariaUsers
        fields = ('name',
                  'email',
                  'age',
                  'medicineType',
                  'id')
