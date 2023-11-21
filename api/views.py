from random import randint

from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .models import FootballModels, LiveLinkModels, FootballScoreModels
from .serializers import FootballSerializer, LinkSerializers, FootballScoreSerializers
from football_app.settings import EMAIL_HOST_USER



# Create your views here.
class FootballView(APIView):

    def get(self, request):
        url = "https://www.scorebat.com/video-api/v3/feed/?token=MTMwOTY0XzE3MDA1NzYyNDlfODEyNTJhYWU0YmZlMDUyNjQ3OWRmZWQ4NDFkMjgxYmEzMTZlMjZmYg=="
        response = requests.get(url)
        result = []
        competition = []
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                for item in data['response']:
                    titles_teams = item.get('title')
                    competitions = item.get('competition')
                    result.append(titles_teams)
                    competition.append(competitions)
            FootballModels.objects.create(teams=result[randint(1, 40)], competition=competition[randint(1, 40)])
            serialized_data = FootballSerializer(FootballModels.objects.all(), many=True)
            return Response(serialized_data.data)


class FootballDatas(APIView):

    def get(self, request):
        score_url = "https://api-football-beta.p.rapidapi.com/teams/statistics"
        score_querystring = {"team": "33", "season": "2019", "league": "39"}
        headers = {
            "X-RapidAPI-Key": "9a8ce634b6msh26029f9ade6f797p117007jsna8172c4a3b0a",
            "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
        }
        url = "https://www.scorebat.com/video-api/v3/feed/?token=MTMwOTY0XzE3MDA1NzYyNDlfODEyNTJhYWU0YmZlMDUyNjQ3OWRmZWQ4NDFkMjgxYmEzMTZlMjZmYg=="
        response = requests.get(url)
        result = []
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                for item in data['response']:
                    titles_teams = item.get('title')
                    result.append(titles_teams)
        responses = requests.get(score_url, headers=headers, params=score_querystring).json()
        score_team_one = responses['response']['fixtures']['wins']['home']
        score_team_two = responses['response']['fixtures']['wins']['away']
        last_score_team_one = responses['response']['fixtures']['draws']['home']
        last_score_team_two = responses['response']['fixtures']['draws']['away']

        # Save the data to the database
        FootballScoreModels.objects.create(teams=result[randint(1, 40)], score_team1=score_team_one,
                                           score_team2=score_team_two,
                                           last_team1_score=last_score_team_one, last_team2_score=last_score_team_two)

        # Serialize the data and return the response
        serialized_data = FootballScoreSerializers(FootballScoreModels.objects.all(), many=True)
        return Response(serialized_data.data)


class LinkView(APIView):
    queryset = LiveLinkModels.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        global match_url
        serializer = LinkSerializers(data=request.data)
        response = LinkSerializers(data=request.data.get('email'))
        Email = str(response.initial_data)
        to_mail = [Email]
        url = "https://www.scorebat.com/video-api/v3/feed/?token" \
              "=MTMwOTY0XzE3MDA1NzYyNDlfODEyNTJhYWU0YmZlMDUyNjQ3OWRmZWQ4NDFkMjgxYmEzMTZlMjZmYg=="
        response = requests.get(url)
        result = []
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                for item in data['response']:
                    match_url = item.get('matchviewUrl')
                    result.append(match_url)
        send_mail('Football App Manager',
                  "Assalomu alaykum xurmatli mijoz, bugun bizni ajoyib  o'yin kutib turmoqda, siz o'yinni 'Jonli' "
                  f"ko'rishingiz mumkin. Mana sizga hozir bo'lib o'tayotgan o'yinni havolasi: {result[0]} ",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
