from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyResponseViewSet, social_involvement_statistics, volunteer_habits, social_involvement_by_education

router = DefaultRouter()
router.register(r'surveyresponses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('social-involvement/', social_involvement_statistics, name='social-involvement-statistics'),
    path('volunteer-habits/', volunteer_habits, name='volunteer-habits'),
    path('social-involvement/education/', social_involvement_by_education, name='social-involvement-by-education'),
]