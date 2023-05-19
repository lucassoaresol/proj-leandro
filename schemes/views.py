from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsAuthRead, IsAuthEmployeeScheme
from .serializers import SchemeSerializer
from .models import Scheme


class SchemeView(generics.ListCreateAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead]


class SchemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead, IsAuthEmployeeScheme]

    def perform_destroy(self, instance: Scheme):
        instance.status = "Canceled"
        instance.finished_at = timezone.now()
        instance.save()
