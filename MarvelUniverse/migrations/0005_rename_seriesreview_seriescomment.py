# Generated by Django 4.2.7 on 2023-11-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarvelUniverse', '0004_seriesreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeriesReview',
            new_name='SeriesComment',
        ),
    ]
