from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    UserProfileListCreateView,
    UserProfileDetailView,

    ListTestsAPIView,
    RetrieveTestAPIView,
    ListActiveTestsAPIView,
    UpdateTestAPIView,
    CreateAnswerAPIView
)


urlpatterns = [
    path('all-profiles', UserProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),

    path('test/all/', ListTestsAPIView.as_view(), name="all-tests"),
    path('test/<str:pk>/', RetrieveTestAPIView.as_view(), name="test-retrieve"),
    path('test/all/active/', ListActiveTestsAPIView.as_view(), name="all-active-tests"),
    path('test/update/<str:pk>/', UpdateTestAPIView.as_view(), name="test-update"),

    path('answer/create/', CreateAnswerAPIView.as_view(), name="answer-create"),
]
