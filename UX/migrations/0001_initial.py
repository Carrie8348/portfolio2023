# Generated by Django 3.2.16 on 2023-02-06 14:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UX_Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(max_length=300)),
                ('created_time', models.CharField(max_length=300)),
                ('tool', models.CharField(max_length=300)),
                ('introduction', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
    ]
