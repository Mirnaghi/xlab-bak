# Generated by Django 3.2.4 on 2021-06-24 10:42

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('status', models.CharField(choices=[('active', 'active'), ('deactive', 'deactive')], default='active', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.CharField(default='cgyngwg', max_length=7)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('edit_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('public', 'public'), ('deactive', 'deactive')], default='active', max_length=15)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]
