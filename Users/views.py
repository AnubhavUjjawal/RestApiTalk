from rest_framework import viewsets
from rest_framework.response import Response
from .models import ApiUser
from .serializers import ApiUserSerializer

class ApiUserViewSet(viewsets.ViewSet):
    """
    A ViewSet for viewing ApiUsers.
    """
    def list(self, request):
        queryset = ApiUser.objects.all()
        serializer = ApiUserSerializer(queryset, many=True)
        return Response(serializer.data)
