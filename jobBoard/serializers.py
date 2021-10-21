from rest_framework import serializers
from .models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = ("__all__")
        # fields = ('company_name', 'company_email', 'job_title', 'job_description',
        #           'salary', 'city', 'state', 'created_at', 'available')