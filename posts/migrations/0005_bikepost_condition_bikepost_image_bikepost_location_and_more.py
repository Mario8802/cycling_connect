# Generated by Django 5.0.4 on 2024-11-23 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_bikepost_image_remove_bikepost_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikepost',
            name='condition',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='bikepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bike_posts/'),
        ),
        migrations.AddField(
            model_name='bikepost',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bikepost',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
