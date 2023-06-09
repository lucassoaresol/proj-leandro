from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import UserView, UserDetailView, UserProfileView, UserUsernameView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/profile/", UserProfileView.as_view()),
    path("users/username/<str:username>/", UserUsernameView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
