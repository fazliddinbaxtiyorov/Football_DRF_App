from rest_framework import serializers
from .models import FootballModels, LiveLinkModels, FootballScoreModels


class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballModels
        fields = '__all__'


class FootballScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = FootballScoreModels
        fields = '__all__'


class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LiveLinkModels
        fields = '__all__'
