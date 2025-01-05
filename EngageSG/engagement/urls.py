from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyResponseViewSet, social_involvement_statistics

router = DefaultRouter()
router.register(r'surveyresponses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes defined in the router
    path('social-involvement/', social_involvement_statistics, name='social-involvement-statistics'),
]