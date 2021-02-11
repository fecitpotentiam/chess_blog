from django.db.models import Q

from .models import Category, Post, Comment


def get_menu_info(request):
    categories = Category.objects.all()
    posts_count_categories = [Post.objects.filter(category=category).count() for category in categories]
    categories = [{'category': category, 'count': count} for category, count in zip(categories, posts_count_categories)]
    latest_posts = Post.objects.all().order_by('-published_date')[:3]
    comments = Comment.objects.all().order_by('-created_date')[:3]

    return {
        'latest_posts': latest_posts,
        'categories': categories,
        'posts_count_categories': posts_count_categories,
        'comments': comments,
    }
