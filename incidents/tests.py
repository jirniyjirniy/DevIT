from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Incident

class IncidentAPITest(APITestCase):
    def setUp(self):
        self.list_url = reverse('incident-list')
        self.valid_payload = {
            'name': 'Test Incident',
            'latitude': 50.45,
            'longitude': 30.52,
            'status': 'ACTIVE'
        }
        self.invalid_payload = {
            'name': '',
            'latitude': 'invalid',
            'longitude': 'invalid',
            'status': 'UNKNOWN'
        }

    def test_create_incident(self):
        response = self.client.post(self.list_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Incident.objects.count(), 1)

    def test_get_incidents(self):
        Incident.objects.create(**self.valid_payload)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_update_incident(self):
        inc = Incident.objects.create(**self.valid_payload)
        url = reverse('incident-detail', args=[inc.id])
        data = {'name': 'Updated Incident', 'status': 'CLOSED'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        inc.refresh_from_db()
        self.assertEqual(inc.name, 'Updated Incident')
        self.assertEqual(inc.status, 'CLOSED')

    def test_delete_incident(self):
        inc = Incident.objects.create(**self.valid_payload)
        url = reverse('incident-detail', args=[inc.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Incident.objects.count(), 0)

    def test_geojson_endpoint(self):
        Incident.objects.create(**self.valid_payload)
        url = reverse('incident-geojson')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('features', response.data)