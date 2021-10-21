from django.urls import path
from .views import JobOfferListCreateAPIView

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name="jobs-list")
]