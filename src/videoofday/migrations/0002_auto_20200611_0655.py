# Generated by Django 3.0.3 on 2020-06-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoofday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
