from django.urls import path
from requests.views import RequestCreateView
from .views import SchemeView, SchemeDetailView

urlpatterns = [
    path("schemes/", SchemeView.as_view()),
    path("schemes/<int:pk>/", SchemeDetailView.as_view()),
    path("schemes/<int:pk>/request/", RequestCreateView.as_view()),
]
