from django.shortcuts import render
from rest_framework import viewsets
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
from rest_framework.response import Response

class SurveyResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data)