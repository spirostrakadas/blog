# Generated by Django 4.1.2 on 2023-04-02 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='number_of_likes',
        ),
    ]
