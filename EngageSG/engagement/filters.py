from django_filters import rest_framework as filters
from .models import SurveyResponse

class SurveyResponseFilter(filters.FilterSet):
    # Human-readable url params
    gender = filters.CharFilter(field_name='Gender_Gender', lookup_expr='exact')
    dwelling = filters.CharFilter(field_name='Dwelling_DwellingType', lookup_expr='exact')
    age_group = filters.CharFilter(field_name='Age2_AgeGroups', lookup_expr='exact')
    industry = filters.CharFilter(field_name='Industry_CurrentIndustry', lookup_expr='exact')

    class Meta:
        model = SurveyResponse
        fields = ['gender', 'dwelling', 'age_group', 'industry']