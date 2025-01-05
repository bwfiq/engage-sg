from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .filters import SurveyResponseFilter

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BaseViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SurveyResponseFilter

    def get_queryset(self):
        queryset = super().get_queryset().order_by('UID_UniqueRespondentID')
        return queryset