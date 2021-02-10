from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

from tinymce import models as tinymce_models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='media/')

    STANDARD = 'S'
    GALLERY = 'G'
    WITHOUT_IMAGE = 'W'

    PREVIEW_FORMAT_CHOICES = [
        (STANDARD, 'Стандартный'),
        (GALLERY, 'Галерея'),
        (WITHOUT_IMAGE, 'Без изображения'),
    ]
    preview_format = models.CharField(
        max_length=1,
        choices=PREVIEW_FORMAT_CHOICES,
        default=STANDARD,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = tinymce_models.HTMLField(verbose_name='Описание')
    address = models.CharField(max_length=300, verbose_name="Место проведения", blank=True)
    datetime = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время мероприятия')
    deadline = models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн подачи заявок')
    payment = models.CharField(max_length=100, verbose_name='Взнос', default="Отсутствует")
    organizer = models.CharField(max_length=100, verbose_name='Организатор', default='Нет информации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Анонс мероприятия'
        verbose_name_plural = 'Анонсы мероприятий'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class PhotoAlbum(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание')
    cover = models.ImageField(verbose_name='Обложка', upload_to='media/')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбомы'


class Photo(models.Model):
  image = models.ImageField(upload_to='media') # здесь укажите куда сохранять изображения
  album = models.ForeignKey(PhotoAlbum, related_name="photo", on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  class Meta:
      verbose_name = 'Фото'
      verbose_name_plural = 'Фото'