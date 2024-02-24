# Generated by Django 5.0.1 on 2024-02-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_featured_news_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/featured_images/'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/featured_images/'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/featured_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/news_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/news_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/news_images/'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/trending_images/'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/trending_images/'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/trending_images/'),
        ),
    ]
