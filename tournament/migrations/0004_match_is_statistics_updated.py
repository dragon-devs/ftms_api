# Generated by Django 4.0.2 on 2023-07-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_match_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_statistics_updated',
            field=models.BooleanField(default=False),
        ),
    ]
