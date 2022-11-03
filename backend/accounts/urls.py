from django.urls import path, include
from .views import GoogleLoginView, RegisterUser, UserDetailView

urlpatterns = [ # api/social/login/
    path("google/", GoogleLoginView.as_view(), name="google"),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/<str:pk>/', UserDetailView.as_view(), name='detail-profile'),
]