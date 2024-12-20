# Generated by Django 5.1.4 on 2024-12-11 21:03

import bike_connect.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, storage=bike_connect.storages.MediaStorage(), upload_to='news_images/', verbose_name='Image')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views Count')),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags for the news article.', max_length=255, null=True, verbose_name='Tags')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Static Page',
                'verbose_name_plural': 'Static Pages',
                'ordering': ['title'],
            },
        ),
    ]
