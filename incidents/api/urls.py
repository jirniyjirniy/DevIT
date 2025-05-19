from rest_framework.routers import DefaultRouter
from django.urls import path, include
from incidents.api.views import IncidentViewSet

router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')

urlpatterns = [
    path('', include(router.urls)),
]