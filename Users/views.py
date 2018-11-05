from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import ApiUser
from .serializers import ApiUserSerializer

class ApiUserList(generics.ListCreateAPIView):
    """
    A ListCreateAPIView for viewing ApiUsers.
    """
    queryset = ApiUser.objects.all()
    serializer_class = ApiUserSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
