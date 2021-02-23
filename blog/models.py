from django.db import models
from django.db.models import signals
from django.utils import timezone

from tinymce import models as tinymce_models


def edit_video_link(sender, instance, **kwargs):
    link = instance.link.replace('watch?v=', '/embed/')
    instance.link = link


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
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


class PostImage(models.Model):
    image = models.ImageField(upload_to='media')  # здесь укажите куда сохранять изображения
    post = models.ForeignKey(Post, related_name="post_image", on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created_date)

    class Meta:
        verbose_name = 'Фото для поста'
        verbose_name_plural = 'Фото для постов'


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
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
  image = models.ImageField(upload_to='media')
  album = models.ForeignKey(PhotoAlbum, related_name="photo", on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return str(self.created_date)

  class Meta:
      verbose_name = 'Фото из альбома'
      verbose_name_plural = 'Фото из альбома'


class QuestionAnswer(models.Model):
    author = models.CharField(max_length=128, verbose_name='Автор')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(null=True, verbose_name='Ответ')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class VideoLesson(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')
    link = models.CharField(max_length=80, verbose_name='Ссылка на Youtube')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеоурок с Youtube'
        verbose_name_plural = 'Видеоуроки с YouTube'


class MainInformation(models.Model):
    main_page_text = tinymce_models.HTMLField(verbose_name='Текст на главной')
    address = models.CharField(max_length=256, verbose_name='Адрес', null=True)
    phone = models.CharField(max_length=16, verbose_name='Телефон')
    email = models.CharField(max_length=32, verbose_name='Email')
    vk_link = models.CharField(max_length=32, verbose_name='Ссылка на ВК')
    instagram_link = models.CharField(max_length=32, verbose_name='Ссылка на Instagram')

    def __str__(self):
        return 'Основная информация'

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'


signals.pre_save.connect(receiver=edit_video_link, sender=VideoLesson)
