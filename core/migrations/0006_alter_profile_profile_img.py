# Generated by Django 4.1.2 on 2023-04-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='defaultuser.webp', null=True, upload_to='profile_images'),
        ),
    ]
