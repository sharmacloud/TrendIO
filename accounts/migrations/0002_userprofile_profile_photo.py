# Generated by Django 2.0.1 on 2018-04-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=' home/Developer/Desktop/TrendIO/'),
        ),
    ]