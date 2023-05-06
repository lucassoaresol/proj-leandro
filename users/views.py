from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .permissions import IsAdminUserCreate, IsAdminUserDestroy, IsAuthEmployee
from .serializers import UserSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUserCreate]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUserDestroy, IsAuthEmployee]

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.save()
