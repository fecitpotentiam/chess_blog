from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import Post, Category, Event, Comment, Photo, PhotoAlbum, PostImage, VideoLesson, QuestionAnswer


class PhotoAdmin(admin.ModelAdmin):
  pass


class PhotoInline(admin.StackedInline):
  model = Photo
  extra = 0


class PhotoAlbumAdmin(admin.ModelAdmin):
  inlines = [PhotoInline,]


class PostImageAdmin(admin.ModelAdmin):
    pass


class PostImageInline(admin.StackedInline):
  model = PostImage
  extra = 0


class PostAdmin(admin.ModelAdmin):
  inlines = [PostImageInline,]


admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(Post, PostAdmin)


for admin_model in [Category, Event, Comment, VideoLesson, QuestionAnswer]:
  admin.site.register(admin_model)
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Event)
# admin.site.register(Comment)


