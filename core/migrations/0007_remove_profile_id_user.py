# Generated by Django 4.1.2 on 2023-04-06 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]