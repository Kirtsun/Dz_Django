# Generated by Django 4.1.2 on 2022-11-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_middleware'),
    ]

    operations = [
        migrations.AddField(
            model_name='middleware',
            name='json',
            field=models.JSONField(default=0),
        ),
    ]
