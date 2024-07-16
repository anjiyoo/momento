# Generated by Django 5.0.7 on 2024-07-15 15:42

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InquiryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=255)),
                ('notice', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_title', models.CharField(max_length=255)),
                ('faq_answer', models.TextField()),
                ('faq_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.faqcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('inquiries_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('inquiry_title', models.CharField(max_length=50)),
                ('inquiry_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.inquirycategory')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='InquiryComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='customer_service.inquiry')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='InquiryImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='inquiry_images/')),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.inquiry')),
            ],
        ),
    ]
