# Generated by Django 5.0.6 on 2024-07-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_remove_dayplan_trip_day_dayplan_trip_delete_tripday'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayplan',
            name='day',
            field=models.DateField(default='2000-10-10'),
            preserve_default=False,
        ),
    ]
