# Generated by Django 4.1.1 on 2022-09-21 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=7, null=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='media/profile_images', verbose_name='Profile Image')),
                ('avaterImage', models.ImageField(blank=True, null=True, upload_to='media/avater_image', verbose_name='Profile Image')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ManyToManyField(blank=True, related_name='userFollower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='userFollowing', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('code', models.CharField(blank=True, max_length=7, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userEmail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
