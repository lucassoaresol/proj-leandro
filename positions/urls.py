from django.urls import path
from .views import PositionView, PositionDetailView

urlpatterns = [
    path("positions/", PositionView.as_view()),
    path("positions/<int:pk>/", PositionDetailView.as_view()),
]
