# Generated by Django 5.1.3 on 2024-11-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikepost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='bikepost',
            name='price',
        ),
        migrations.AddField(
            model_name='bikepost',
            name='category',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('repair', 'Repair'), ('accessories', 'Accessories')], default='buy', max_length=20),
        ),
    ]