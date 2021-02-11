from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Category, Event, Comment, Photo, PhotoAlbum


class PhotoAdmin(admin.ModelAdmin):
  pass


class PhotoInline(admin.StackedInline):
  model = Photo
  extra = 0


class PhotoAlbumAdmin(admin.ModelAdmin):
  inlines = [PhotoInline,]


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)