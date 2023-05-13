from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .permissions import IsReleaseUserCreate, IsAdminUserDestroy, IsAuthEmployee
from .serializers import UserSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("is_active", "is_expired")
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsReleaseUserCreate]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUserDestroy, IsAuthEmployee]

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.is_expired = True
        instance.date_expired = timezone.now()
        instance.save()


class UserProfileView(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return User.objects.filter(id=user_id)


class UserUsernameView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs["username"]
        return User.objects.filter(username__iexact=username).first()
