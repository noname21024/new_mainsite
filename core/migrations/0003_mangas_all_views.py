# Generated by Django 5.0.2 on 2024-03-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_chapters_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangas',
            name='all_views',
            field=models.IntegerField(default=0),
        ),
    ]
