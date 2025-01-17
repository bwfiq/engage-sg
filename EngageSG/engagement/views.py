from django.shortcuts import render
from rest_framework import viewsets
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Q, Avg
from collections import defaultdict
from .base_views import BaseViewSet
from .base_views import BaseViewSet
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Q
from collections import defaultdict

class SurveyResponseViewSet(BaseViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data)

class SocialInvolvementStatisticsView(BaseViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        responses = SurveyResponse.objects.values('Age2_AgeGroups', 'Gender_Gender').annotate(
            sports_group=Count('SocialInvolve_SportsGroupParticipation', filter=Q(SocialInvolve_SportsGroupParticipation='Yes')),
            arts_group=Count('SocialInvolve_ArtsCulturalGroupParticipation', filter=Q(SocialInvolve_ArtsCulturalGroupParticipation='Yes')),
            community_group=Count('SocialInvolve_CommunityGroupParticipation', filter=Q(SocialInvolve_CommunityGroupParticipation='Yes')),
            welfare_group=Count('SocialInvolve_WelfareSelfHelpGroupParticipation', filter=Q(SocialInvolve_WelfareSelfHelpGroupParticipation='Yes')),
            religious_group=Count('SocialInvolve_ReligiousGroupParticipation', filter=Q(SocialInvolve_ReligiousGroupParticipation='Yes'))
        )

        total_responses = SurveyResponse.objects.count()
        statistics = defaultdict(dict)

        for response in responses:
            age_group = response['Age2_AgeGroups']
            Gender_Gender = response['Gender_Gender']
            statistics[age_group][Gender_Gender] = {
                'sports_group': f"{(response['sports_group'] / total_responses) * 100:.2f}%",
                'arts_group': f"{(response['arts_group'] / total_responses) * 100:.2f}%",
                'community_group': f"{(response['community_group'] / total_responses) * 100:.2f}%",
                'welfare_group': f"{(response['welfare_group'] / total_responses) * 100:.2f}%",
                'religious_group': f"{(response['religious_group'] / total_responses) * 100:.2f}%"
            }

        return Response(statistics)

class VolunteerHabitsView(BaseViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    @action(detail=False, methods=['get'])
    def habits(self, request):
        responses = SurveyResponse.objects.values('VolunteerDonateFreq_FrequencyOfVolunteering', 'Gender_Gender').annotate(
            total_volunteers=Count('VolunteerDonate_VolunteeredTime', filter=Q(VolunteerDonate_VolunteeredTime='Yes')),
            common_activity=Count('VolunteerDonate_DonatedMoney', filter=Q(VolunteerDonate_DonatedMoney='Yes')),
        )

        stats = []
        for response in responses:
            stats.append({
                'VolunteerDonateFreq_FrequencyOfVolunteering': response['VolunteerDonateFreq_FrequencyOfVolunteering'],
                'Gender_Gender': response['Gender_Gender'],
                'total_volunteers': response.get('total_volunteers', 0),
                'common_activity': response.get('common_activity', 0),
            })

        return Response(stats)

class SocialInvolvementByEducationView(BaseViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    @action(detail=False, methods=['get'])
    def by_education(self, request):
        responses = SurveyResponse.objects.values('HighestEd_HighestEducationLevel').annotate(
            sports_group=Count('SocialInvolve_SportsGroupParticipation', filter=Q(SocialInvolve_SportsGroupParticipation='Yes')),
            arts_group=Count('SocialInvolve_ArtsCulturalGroupParticipation', filter=Q(SocialInvolve_ArtsCulturalGroupParticipation='Yes')),
            community_group=Count('SocialInvolve_CommunityGroupParticipation', filter=Q(SocialInvolve_CommunityGroupParticipation='Yes')),
            welfare_group=Count('SocialInvolve_WelfareSelfHelpGroupParticipation', filter=Q(SocialInvolve_WelfareSelfHelpGroupParticipation='Yes')),
            religious_group=Count('SocialInvolve_ReligiousGroupParticipation', filter=Q(SocialInvolve_ReligiousGroupParticipation='Yes'))
        )

        total_responses = SurveyResponse.objects.count()

        statistics = {response['HighestEd_HighestEducationLevel']: {
            'sports_group': f"{(response['sports_group'] / total_responses) * 100:.2f}%",
            'arts_group': f"{(response['arts_group'] / total_responses) * 100:.2f}%",
            'community_group': f"{(response['community_group'] / total_responses) * 100:.2f}%",
            'welfare_group': f"{(response['welfare_group'] / total_responses) * 100:.2f}%",
            'religious_group': f"{(response['religious_group'] / total_responses) * 100:.2f}%",
        } for response in responses}

        return Response(statistics)
    
class OutcomeConnectionsView(BaseViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    @action(detail=False, methods=['get'])
    def connections(self, request):
        responses = (SurveyResponse.objects
                     .values('Age2_AgeGroups', 'Gender_Gender')
                     .annotate(
                         average_score=Avg('OutcomeConnection_StrengthOfConnectionToSG')
                     ))

        connections = defaultdict(dict)

        for response in responses:
            age_group = response['Age2_AgeGroups']
            gender = response['Gender_Gender']
            connections[age_group][gender] = {
                'average_score': f"{response['average_score']:.2f}"
            }

        return Response(connections)