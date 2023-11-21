from django.db import models


# Create your models here.

class FootballModels(models.Model):
    teams = models.CharField(max_length=100)
    competition = models.CharField(max_length=60)


class FootballScoreModels(models.Model):
    teams = models.CharField(max_length=100)
    score_team1 = models.CharField(max_length=100)
    score_team2 = models.CharField(max_length=100)
    last_team1_score = models.CharField(max_length=100)
    last_team2_score = models.CharField(max_length=100)


class LiveLinkModels(models.Model):
    email = models.EmailField(max_length=120)
