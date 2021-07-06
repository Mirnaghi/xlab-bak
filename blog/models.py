from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import random
import string

statuses = [
    ('active', 'active'),
    ('deactive', 'deactive')
]


def set_image_filename(instance, filename):
    return f"cover_images/post_{instance.id}/{filename}"

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=55)
    status = models.CharField(max_length=15, default=statuses[0][0], choices=statuses)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_statuses = [
        ('pending', 'pending'),
        ('public', 'public'),
        ('deactive', 'deactive')
    ]

    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    slug = models.CharField(max_length=7, default=''.join(random.choices(string.ascii_lowercase, k=7)))
    cover_img = models.ImageField(upload_to=set_image_filename, default='cover_images/default.jpg')
    publish_date = models.DateField(default=timezone.now)
    edit_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(User)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=15, default=statuses[0][0], choices=post_statuses)

    objects = models.Manager()

    def __str__(self):
        return self.title


# class Image(models.Model):
#     post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
#     src = models.ImageField(upload_to=)
#     status = models.CharField(max_length=15, default=statuses[0][0], choices=statuses)

#     def __str__(self):
#         return str(self.src)
