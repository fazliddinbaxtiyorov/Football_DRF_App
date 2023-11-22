# Generated by Django 4.2.7 on 2023-11-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.CharField(max_length=100)),
                ('competition', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='FootballScoreModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.CharField(max_length=100)),
                ('score_team1', models.CharField(max_length=100)),
                ('score_team2', models.CharField(max_length=100)),
                ('last_team1_score', models.CharField(max_length=100)),
                ('last_team2_score', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LiveLinkModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
            ],
        ),
    ]
