# Generated by Django 4.2.4 on 2023-08-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0025_alter_groupclub_group_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupclub',
            name='group_table_number',
            field=models.IntegerField(default=0),
        ),
    ]
