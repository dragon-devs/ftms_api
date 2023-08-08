# Generated by Django 4.0.2 on 2023-07-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=255)),
                ('captain_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('payment', models.BooleanField()),
                ('club_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
