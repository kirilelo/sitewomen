# Generated by Django 5.0.3 on 2024-06-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_boobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='boobs',
        ),
    ]
