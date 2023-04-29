from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsAuthRead, IsAuthEmployeeScheme
from departments.models import Department
from .serializers import SchemeSerializer
from .models import Scheme


class SchemeView(generics.ListAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead]


class SchemeCreateView(generics.CreateAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead]

    def perform_create(self, serializer):
        department = get_object_or_404(Department, id=self.kwargs["pk"])

        return serializer.save(department=department)


class SchemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead, IsAuthEmployeeScheme]

    def perform_destroy(self, instance: Scheme):
        instance.status = "Canceled"
        instance.finished_at = timezone.now()
        instance.save()
