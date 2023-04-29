from django.urls import path
from .views import SchemeView, SchemeDetailView

urlpatterns = [
    path("schemes/", SchemeView.as_view()),
    path("schemes/<int:pk>/", SchemeDetailView.as_view()),
]
