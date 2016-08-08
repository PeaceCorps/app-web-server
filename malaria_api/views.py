from malaria_web.models import Post, MalariaUsers
from malaria_api.serializers import PostSerializer, MalariaUserSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post endpoint that provides `list` and `detail` actions
    `list` action returns a list of all Posts
    `detail` action returns a particular Post instance based on id
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MalariaUsersViewSet(viewsets.ModelViewSet):

    queryset = MalariaUsers.objects.all()
    serializer_class = MalariaUserSerializer


@api_view(['GET', 'POST'])
def muser_list(request):
    if request.method == 'GET':
        muser = MalariaUsers.objects.all()
        serializer = MalariaUserSerializer(muser, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MalariaUserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a pcuser instance.
@api_view(['GET', 'PUT', 'DELETE'])
def muser_detail(request, pk):
    try:
        pcuser = MalariaUsers.objects.get(pk=pk)
    except MalariaUsers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MalariaUserSerializer(pcuser)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MalariaUserSerializer(pcuser, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        muser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
