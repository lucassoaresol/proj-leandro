from django.urls import path
from schemes.views import SchemeCreateView
from .views import DepartmentView, DepartmentDetailView

urlpatterns = [
    path("departments/", DepartmentView.as_view()),
    path("departments/<int:pk>/", DepartmentDetailView.as_view()),
    path("departments/<int:pk>/scheme/", SchemeCreateView.as_view()),
]
