# Generated by Django 5.0.3 on 2024-07-16 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0006_accommodationlike'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='accommodation_type',
            field=models.CharField(blank=True, choices=[('pension_pool_vila', '펜션, 풀빌라'), ('camping_glamping', '캠핑, 글램핑'), ('boutique_motel', '부티크 모텔')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]