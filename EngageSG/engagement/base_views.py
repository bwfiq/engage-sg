from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticated

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BaseViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset().order_by('UID_UniqueRespondentID')
        # add filtering later
        return queryset