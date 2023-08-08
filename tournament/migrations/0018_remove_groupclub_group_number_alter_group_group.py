# Generated by Django 4.2.4 on 2023-08-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0017_alter_groupclub_options_groupclub_group_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupclub',
            name='group_number',
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(choices=[('A', 'Group A'), ('B', 'Group B'), ('C', 'Group C'), ('D', 'Group D'), ('E', 'Group E'), ('F', 'Group F'), ('G', 'Group G'), ('H', 'Group H'), ('I', 'Group I'), ('J', 'Group J'), ('K', 'Group K'), ('L', 'Group L'), ('M', 'Group M'), ('N', 'Group N'), ('O', 'Group O'), ('P', 'Group P')], max_length=1),
        ),
    ]