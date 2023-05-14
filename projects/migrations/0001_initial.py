# Generated by Django 4.2.1 on 2023-05-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('project_image', models.ImageField(upload_to='project')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('gihubLink', models.CharField(blank=True, max_length=255, null=True)),
                ('live_link', models.CharField(blank=True, max_length=255, null=True)),
                ('serversite', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]