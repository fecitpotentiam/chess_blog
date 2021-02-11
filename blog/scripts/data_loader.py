import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chess_coach_blog.settings")
django.setup()

from blog.models import *

posts = Post.objects.all()

for post in posts:
    print(post)

