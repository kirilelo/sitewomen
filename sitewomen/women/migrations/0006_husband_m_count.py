# Generated by Django 5.0.3 on 2024-06-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_alter_women_husband'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]