# Generated by Django 3.2.4 on 2021-07-05 12:25

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(default='cover_images/default.jpg', upload_to=blog.models.set_image_filename),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default='fjdfnzv', max_length=7),
        ),
    ]
