# Generated by Django 4.1.1 on 2022-10-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenge', '0003_alter_challenge_minimumvote_alter_challenge_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='eight_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='firth_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='forth_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='seven_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='six_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='tenth_place_reward',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
