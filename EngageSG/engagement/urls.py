from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyResponseViewSet, social_involvement_statistics, volunteer_habits

router = DefaultRouter()
router.register(r'surveyresponses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('social-involvement/', social_involvement_statistics, name='social-involvement-statistics'),
    path('volunteer-habits/', volunteer_habits, name='volunteer-habits'),  # Add this line
]