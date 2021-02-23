from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import(Post, Category, Event, Comment, Photo, PhotoAlbum, PostImage, VideoLesson, QuestionAnswer,
  MainInformation)


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


class MainInformationAdmin(admin.ModelAdmin):
  model = MainInformation

  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    return True if num_objects <= 1 else False


admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(MainInformation, MainInformationAdmin)


for admin_model in [Category, Event, Comment, VideoLesson, QuestionAnswer]:
  admin.site.register(admin_model)
