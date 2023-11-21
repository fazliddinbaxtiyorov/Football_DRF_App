from django.contrib import admin
from .models import FootballModels, FootballScoreModels
# Register your models here.
admin.site.register(FootballModels)
admin.site.register(FootballScoreModels)
