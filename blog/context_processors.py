from django.db.models import Q, Count

from .models import Category, Post


def get_menu_info(request):
    categories = Category.objects.all()
    posts_count_categories = [Post.objects.filter(category=category).count() for category in categories]
    categories = [{'category': category, 'count': count} for category, count in zip(categories, posts_count_categories)]
    latest_posts = Post.objects.all().order_by('-published_date')[:3]
    archived_posts = Post.objects.values('published_date__year').order_by(
        '-published_date__year'
    ).annotate(count=Count('id'))

    return {
        'latest_posts': latest_posts,
        'categories': categories,
        'posts_count_categories': posts_count_categories,
        'archived_posts': archived_posts
    }
