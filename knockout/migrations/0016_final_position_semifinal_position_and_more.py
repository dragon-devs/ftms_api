# Generated by Django 4.2.4 on 2023-08-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knockout', '0015_alter_qualifyteam_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='final',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='semifinal',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='thirdplace',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]