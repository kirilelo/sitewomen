# Generated by Django 5.0.3 on 2024-06-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='boobs',
            field=models.IntegerField(default=3),
        ),
    ]
