# Generated by Django 4.1.2 on 2023-04-01 14:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded')),
                ('caption', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('number_of_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('profile_img', models.ImageField(upload_to='profile_images')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
