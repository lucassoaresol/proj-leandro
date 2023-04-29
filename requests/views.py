from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from users.permissions import IsAuthEmployeeRequest
from schemes.models import Scheme
from .serializers import RequestSerializer
from .models import Request


class RequestView(generics.ListAPIView):
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Request.objects.all()
        if self.request.user.role == "Manager":
            return Request.objects.filter(
                scheme__department=self.request.user.department
            )
        return Request.objects.filter(user=self.request.user)


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        scheme = get_object_or_404(Scheme, id=self.kwargs["pk"])

        if not scheme.status == "Open":
            raise PermissionDenied("does not accept new requests")

        if not scheme.department == self.request.user.department:
            raise PermissionDenied("User without permission")

        return serializer.save(scheme=scheme, user=self.request.user)


class RequestDetailView(generics.RetrieveDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthEmployeeRequest]

    def perform_destroy(self, instance: Request):
        if not instance.scheme.status == "Open":
            raise PermissionDenied("request can no longer be canceled")
        instance.is_active = False
        instance.canceled_at = timezone.now()
        instance.save()
