# Generated by Django 3.0.8 on 2020-08-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationshipapp', '0002_publications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='article',
        ),
        migrations.AddField(
            model_name='publications',
            name='article',
            field=models.ManyToManyField(to='relationshipapp.Article'),
        ),
    ]
