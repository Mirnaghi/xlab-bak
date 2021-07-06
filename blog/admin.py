from django.contrib import admin
from .models import Post, Category

# Register your models here.


# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 1


# class PostAdmin(admin.ModelAdmin):
#     inlines = [ImageInline]


admin.site.register(Post)
admin.site.register(Category)
