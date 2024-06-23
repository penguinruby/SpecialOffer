# Generated by Django 5.0.6 on 2024-06-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_number', models.CharField(blank=True, max_length=255, null=True)),
                ('product_number_2', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_url', models.URLField(blank=True, max_length=500, null=True)),
                ('product_picture_url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
