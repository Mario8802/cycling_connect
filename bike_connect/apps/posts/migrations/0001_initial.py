# Generated by Django 5.1.4 on 2024-12-11 21:03

import bike_connect.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('repair', 'Repair'), ('accessories', 'Accessories')], default='buy', max_length=20)),
                ('condition', models.CharField(blank=True, choices=[('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')], max_length=15, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, help_text='Optional image for the post.', max_length=255, null=True, storage=bike_connect.storages.MediaStorage(), upload_to='bike_posts/', verbose_name='Post Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
