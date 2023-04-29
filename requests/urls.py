from django.urls import path
from .views import RequestView, RequestDetailView

urlpatterns = [
    path("requests/", RequestView.as_view()),
    path("requests/<int:pk>/", RequestDetailView.as_view()),
]
