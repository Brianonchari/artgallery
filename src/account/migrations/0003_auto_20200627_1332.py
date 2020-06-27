# Generated by Django 2.2 on 2020-06-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='artist_type',
            field=models.CharField(default='Sketch Artist', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.CharField(default='This is my short bio', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='full_name',
            field=models.CharField(default='Brian Onchari', max_length=50),
            preserve_default=False,
        ),
    ]