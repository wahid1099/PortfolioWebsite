# Generated by Django 4.2.1 on 2023-05-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=250)),
                ('blog_image', models.ImageField(upload_to='project')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('descriptions', models.CharField(max_length=500)),
                ('live_link', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
