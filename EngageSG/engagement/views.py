from django.shortcuts import render
from rest_framework import viewsets
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Q
from collections import defaultdict

class SurveyResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data)

@api_view(['GET'])
def social_involvement_statistics(request):
    responses = SurveyResponse.objects.values('age_2', 'gender').annotate(
        sports_group=Count('social_involve_1', filter=Q(social_involve_1='Yes')),
        arts_group=Count('social_involve_2', filter=Q(social_involve_2='Yes')),
        community_group=Count('social_involve_3', filter=Q(social_involve_3='Yes')),
        welfare_group=Count('social_involve_4', filter=Q(social_involve_4='Yes')),
        religious_group=Count('social_involve_5', filter=Q(social_involve_5='Yes'))
    )

    total_responses = SurveyResponse.objects.count()
    statistics = defaultdict(dict)
    
    for response in responses:
        age_group = response['age_2']
        gender = response['gender']
        statistics[age_group][gender] = {
            'sports_group': f"{(response['sports_group'] / total_responses) * 100:.2f}%",
            'arts_group': f"{(response['arts_group'] / total_responses) * 100:.2f}%",
            'community_group': f"{(response['community_group'] / total_responses) * 100:.2f}%",
            'welfare_group': f"{(response['welfare_group'] / total_responses) * 100:.2f}%",
            'religious_group': f"{(response['religious_group'] / total_responses) * 100:.2f}%"
        }

    return Response(statistics)