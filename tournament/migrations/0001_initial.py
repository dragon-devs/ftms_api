# Generated by Django 4.0.2 on 2023-07-23 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ftms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('A', 'Group A'), ('B', 'Group B'), ('C', 'Group C'), ('D', 'Group D'), ('E', 'Group E'), ('F', 'Group F'), ('G', 'Group G'), ('H', 'Group H'), ('I', 'Group I'), ('J', 'Group J'), ('K', 'Group K'), ('L', 'Group L'), ('M', 'Group M'), ('N', 'Group N'), ('O', 'Group O'), ('P', 'Group P'), ('Q', 'Group Q')], max_length=1)),
                ('matches_count', models.PositiveIntegerField(default=0)),
                ('group_club_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_1', to='ftms.club')),
                ('group_club_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_2', to='ftms.club')),
                ('group_club_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_3', to='ftms.club')),
                ('group_club_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_4', to='ftms.club')),
            ],
        ),
        migrations.CreateModel(
            name='GroupClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.PositiveIntegerField(default=0)),
                ('wins', models.PositiveIntegerField(default=0)),
                ('draw', models.PositiveIntegerField(default=0)),
                ('lose', models.PositiveIntegerField(default=0)),
                ('gf', models.PositiveIntegerField(default=0)),
                ('ga', models.PositiveIntegerField(default=0)),
                ('gd', models.IntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('club_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='ftms.club')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tournament.group')),
            ],
        ),
        migrations.CreateModel(
            name='MyTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('teams_selection', models.CharField(choices=[('8', 8), ('16', 16), ('32', 32), ('64', 64)], max_length=2)),
                ('tournament_type', models.CharField(choices=[('Groups', 'Groups & Knockout'), ('K/O', 'Knockout')], max_length=8)),
                ('current_stage', models.CharField(choices=[('Group', 'Group Stage'), ('Round16', 'Round of 16'), ('QuarterFinal', 'Quarter Final'), ('SemiFinal', 'Semi Final'), ('Final', 'Final')], default='Group', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('team_1_score', models.PositiveIntegerField(blank=True, null=True)),
                ('team_2_score', models.PositiveIntegerField(blank=True, null=True)),
                ('is_match_ended', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='tournament.group')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_matches', to='tournament.groupclub')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_matches', to='tournament.groupclub')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.mytournament')),
            ],
        ),
        migrations.AddField(
            model_name='groupclub',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.mytournament'),
        ),
        migrations.AddField(
            model_name='group',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='tournament.mytournament'),
        ),
        migrations.CreateModel(
            name='ClubHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='ftms.club')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.mytournament')),
            ],
        ),
    ]
