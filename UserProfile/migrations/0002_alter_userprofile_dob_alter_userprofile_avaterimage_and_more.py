# Generated by Django 4.1.1 on 2022-09-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='DOB',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avaterImage',
            field=models.ImageField(blank=True, null=True, upload_to='media/avater_image', verbose_name='Avater Image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
