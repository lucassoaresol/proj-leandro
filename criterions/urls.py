from django.urls import path
from .views import CriterionView, CriterionDetailView

urlpatterns = [
    path("criterions/", CriterionView.as_view()),
    path("criterions/<int:pk>/", CriterionDetailView.as_view()),
]
