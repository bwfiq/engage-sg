from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyResponseViewSet

router = DefaultRouter()
router.register(r'surveyresponses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes defined in the router
]