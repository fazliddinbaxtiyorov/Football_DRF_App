from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class FootballViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_teams(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_datas(self):
        response = self.client.get('/api/score')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_link(self):
        response = self.client.get('/api/link')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_error(self):
        response = self.client.get('/api/qwerty')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)