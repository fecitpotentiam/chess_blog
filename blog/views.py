from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .models import Post, Category, Event, Comment, PhotoAlbum, Photo
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog.html',
                  {
                      'page_title': 'Блог',
                      'posts': posts,
                  })


def category_post_list(request, pk):
    posts = Post.objects.filter(category__pk=pk).order_by('-published_date')
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog.html',
                  {
                      'page_title': category.title,
                      'posts': posts,
                  })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post__pk=pk).order_by('-created_date')
    print(comments)
    return render(request, 'post.html', {'post': post, 'comments': comments})


def events_list(request):
    events = Event.objects.all().order_by('-datetime')
    return render(request, 'events.html',
                  {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_single.html', {'event': event})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(request.method)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post.html', {'form': form})


def get_albums(request):
    albums = PhotoAlbum.objects.all().order_by('-created_date')
    return render(request, 'albums.html', {'albums': albums})


def get_photos_in_album(request, pk):
    photos = Photo.objects.filter(album__pk=pk).order_by('-created_date')
    album_name = photos[0].album
    return render(request, 'album_photos.html', {'photos': photos, 'album_name': album_name})


def youtube_videos(request):
    return render(request, 'videolessons.html', {'test': 'test'})