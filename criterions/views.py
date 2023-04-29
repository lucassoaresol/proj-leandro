from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsAuthRead
from .serializers import CriterionSerializer
from .models import Criterion


class CriterionView(generics.ListCreateAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead]


class CriterionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthRead]
