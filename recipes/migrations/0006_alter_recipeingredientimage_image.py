# Generated by Django 4.1.7 on 2023-03-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipeingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
    ]
