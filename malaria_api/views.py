from rest_framework import viewsets
from malaria.models import Post
from malaria_api.serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post endpoint that provides `list` and `detail` actions
    `list` action returns a list of all Posts
    `detail` action returns a particular Post instance based on id
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
