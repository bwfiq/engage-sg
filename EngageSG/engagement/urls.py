from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyResponseViewSet, SocialInvolvementStatisticsView, VolunteerHabitsView, SocialInvolvementByEducationView

router = DefaultRouter()
router.register(r'surveyresponses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('social-involvement/statistics/', SocialInvolvementStatisticsView.as_view({'get': 'statistics'}), name='social-involvement-statistics'),
    path('volunteer-habits/', VolunteerHabitsView.as_view({'get': 'habits'}), name='volunteer-habits'),
    path('social-involvement/education/', SocialInvolvementByEducationView.as_view({'get': 'by_education'}), name='social-involvement-by-education'),
]