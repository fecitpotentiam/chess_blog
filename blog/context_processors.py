from .models import Category, Post, Comment


def get_menu_info(request):
    categories = Category.objects.all()
    latest_posts = Post.objects.all().order_by('-published_date')[:3]
    comments = Comment.objects.all().order_by('-created_date')[:3]

    return {
        'latest_posts': latest_posts,
        'categories': categories,
        'comments': comments
    }