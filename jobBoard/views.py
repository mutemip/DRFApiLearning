from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobOffer
from .serializers import JobOfferSerializer


class JobOfferListCreateAPIView(APIView):

    def get(self, request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

