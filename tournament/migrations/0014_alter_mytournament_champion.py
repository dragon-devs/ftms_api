# Generated by Django 4.0.2 on 2023-07-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0013_alter_mytournament_champion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytournament',
            name='champion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
