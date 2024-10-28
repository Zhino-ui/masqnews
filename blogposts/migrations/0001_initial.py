# Generated by Django 5.1.2 on 2024-10-23 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_home_banner_top', models.BooleanField(default=False)),
                ('is_home_banner_center', models.BooleanField(default=False)),
                ('is_home_banner_bottom', models.BooleanField(default=False)),
                ('is_category_banner', models.BooleanField(default=False)),
                ('is_side_banner', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=255)),
                ('writer_image', models.ImageField(default='images/images_4.jpg', upload_to='images/')),
                ('is_featured', models.BooleanField(default=False)),
                ('is_latest', models.BooleanField(default=False)),
                ('is_banner', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blogposts.category')),
            ],
        ),
    ]
