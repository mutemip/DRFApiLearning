from django.urls import path
from .views import JobOfferListCreateAPIView, JobOfferDetailAPIView

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name="jobs-list"),
    path('job-details/<int:pk>/', JobOfferDetailAPIView.as_view(), name="jobs-detail")
]