from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import FootballModels


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


class TestModels(TestCase):
    def setUp(self) -> None:
        FootballModels.objects.create(teams="Montserrat - Barbados",
                                      competition="EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        FootballModels.objects.create(teams="Denmark U-19 - France U-19",
                                      competition="EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        FootballModels.objects.create(teams="Norway U-17 - France U-17",
                                      competition="CONCACAF: Nations League, League C")
        FootballModels.objects.create(teams="Levante - Racing Santander",
                                      competition="CONCACAF: Nations League, League C")
        FootballModels.objects.create(teams="Kyrgyzstan - Oman", competition="WORLD CUP: Asia. 2nd round")
        FootballModels.objects.create(teams="Rukh Lviv - Shakhtar D", competition="WORLD CUP: Asia. 2nd round")

    def test_teams(self):
        obj1 = FootballModels.objects.get(teams='Kyrgyzstan - Oman')
        obj2 = FootballModels.objects.get(teams="Denmark U-19 - France U-19")
        obj3 = FootballModels.objects.get(teams="Norway U-17 - France U-17", )
        obj4 = FootballModels.objects.get(teams="Levante - Racing Santander")
        self.assertEquals(obj1.teams, "Kyrgyzstan - Oman")
        self.assertEquals(obj2.teams, "Denmark U-19 - France U-19")
        self.assertEquals(obj3.teams, "Norway U-17 - France U-17")
        self.assertEquals(obj4.teams, "Levante - Racing Santander")

    def test_competition(self):
        obj1 = FootballModels.objects.get(competition="EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        obj2 = FootballModels.objects.get(competition="EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        obj3 = FootballModels.objects.get(competition="CONCACAF: Nations League, League C")
        obj4 = FootballModels.objects.get(competition="CONCACAF: Nations League, League C")
        self.assertEquals(obj1.competition, "EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        self.assertEquals(obj2.competition, "EUROPE: UNDER-19 CHAMPIONSHIP: Qualifying round, Group Stage")
        self.assertEquals(obj3.competition, "CONCACAF: Nations League, League C")
        self.assertEquals(obj4.competition, "CONCACAF: Nations League, League C")
