# Generated by Django 5.0.6 on 2024-07-18 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=10, verbose_name='도시그룹')),
                ('first_town_name', models.CharField(max_length=10, verbose_name='첫번째 도시명')),
                ('second_town_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='두번쨰 도시명')),
                ('third_town_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='세번째 도시명')),
            ],
        ),
        migrations.CreateModel(
            name='CountyImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='travel/%Y/%m', verbose_name='도시이미지')),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.county')),
            ],
        ),
    ]
