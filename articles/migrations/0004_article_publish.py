# Generated by Django 4.1.7 on 2023-03-15 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_timestamp_article_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
