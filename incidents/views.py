from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Incident
from .serializers import IncidentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=False, methods=['get'], url_path='geojson')
    def geojson(self, request):
        active = Incident.objects.filter(status='ACTIVE')
        features = []
        for inc in active:
            features.append({
                'type': 'Feature',
                'properties': {
                    'id': inc.id,
                    'name': inc.name,
                    'status': inc.status,
                    'created_at': inc.created_at.isoformat(),
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(inc.longitude), float(inc.latitude)],
                }
            })
        return Response({
            'type': 'FeatureCollection',
            'features': features
        })