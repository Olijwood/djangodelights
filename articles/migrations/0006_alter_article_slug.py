# Generated by Django 4.1.7 on 2023-03-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_slug_alter_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
