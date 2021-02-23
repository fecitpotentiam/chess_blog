from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .models import Post, Category, Event, Comment, MainInformation, PhotoAlbum, Photo, PostImage, VideoLesson, QuestionAnswer
from .forms import CommentForm, QuestionForm


def index(request):
    information = MainInformation.objects.all().first()
    return render(request, 'about.html', {'information': information})


def paginate(request, posts):
    paginator = Paginator(posts, 10)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')

    posts = paginate(request, posts)

    return render(request, 'blog/blog.html',
                  {
                      'page_title': 'Блог',
                      'posts': posts,
                  })


def category_post_list(request, pk):
    posts = Post.objects.filter(category__pk=pk).order_by('-published_date')
    posts = paginate(request, posts)

    category = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/blog.html',
                  {
                      'page_title': category.title,
                      'posts': posts,
                  })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post__pk=pk).order_by('-created_date')
    photos = PostImage.objects.filter(post=post)
    return render(request, 'blog/blog-single.html', {'post': post, 'comments': comments, 'photos': photos})


def events_list(request):
    events = Event.objects.all().order_by('-datetime')
    paginator = Paginator(events, 6)

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    return render(request, 'events.html',
                  {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event-single.html', {'event': event})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/blog-single.html', {'form': form})


def search(request):
    if request.method == "POST":
        query = request.POST['query']

        posts = Post.objects.filter(text__contains=query)
        posts = paginate(request, posts)

        return render(request, 'blog/blog.html',
                      {
                          'page_title': f'Поиск по запросу: {query}',
                          'posts': posts,
                      })
    else:
        return redirect('post_list')


def get_albums(request):
    albums = PhotoAlbum.objects.all().order_by('-created_date')
    paginator = Paginator(albums, 6)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    return render(request, 'gallery.html', {'albums': albums})


def get_photos_in_album(request, pk):
    photos = Photo.objects.filter(album__pk=pk).order_by('-created_date')
    album_name = photos[0].album if photos else "Пустой альбом"
    return render(request, 'album.html', {'photos': photos, 'album_name': album_name})


def youtube_videos(request):
    videos = VideoLesson.objects.all().order_by('-published_date')
    paginator = Paginator(videos, 6)

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videolessons.html', {'videos': videos})


def archived_posts(request, pk: int):
    posts = Post.objects.filter(published_date__year=pk).order_by('-published_date')
    posts = paginate(request, posts)

    return render(request, 'blog/blog.html',
                  {
                      'page_title': f'Записи за {pk} год',
                      'posts': posts,
                  })


def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('thanks')
    else:
        return redirect('post_list')


def question_answer(request):
    questions = QuestionAnswer.objects.all().order_by('-published_date')

    paginator = Paginator(questions, 10)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'question-answer.html', {'questions': questions})


def thanks(request):
    return render(request, 'thanks.html')


def book(request):
    return render(request, 'book.html')


def contacts(request):
    return render(request, 'contact.html')

