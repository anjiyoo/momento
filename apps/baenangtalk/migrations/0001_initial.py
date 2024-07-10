# Generated by Django 5.0.6 on 2024-07-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baenangtalk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bae_title', models.CharField(max_length=100, verbose_name='제목')),
                ('bae_content', models.TextField(verbose_name='내용')),
                ('bae_img', models.ImageField(upload_to='baenangtalk/img', verbose_name='이미지')),
                ('bae_like', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bae_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
        migrations.CreateModel(
            name='BaenangtalkComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bae_com_content', models.CharField(max_length=100, verbose_name='내용')),
                ('bae_com_like', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bae_com_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
        migrations.CreateModel(
            name='BaenangtalkPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bae_month', models.DateField(verbose_name='월')),
            ],
        ),
        migrations.CreateModel(
            name='BaenangtalkSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bae_sub_name', models.CharField(max_length=10, verbose_name='주제명')),
            ],
        ),
    ]