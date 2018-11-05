from rest_framework import generics
from rest_framework.response import Response
from .models import ApiUser
from .serializers import ApiUserSerializer

class ApiUserViewSet(generics.ListAPIView):
    """
    A ViewSet for viewing ApiUsers.
    get:
        Lists ApiUsers
    """
    def get(self, request):
        queryset = ApiUser.objects.all()
        serializer = ApiUserSerializer(queryset, many=True)
        return Response(serializer.data)
