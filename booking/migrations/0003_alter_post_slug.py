# Generated by Django 3.2.20 on 2023-08-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230824_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]