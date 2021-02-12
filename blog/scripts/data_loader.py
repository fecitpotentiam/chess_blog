import os
from os import listdir
from shutil import copyfile

from django.utils import timezone
import pytz
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chess_coach_blog.settings")
django.setup()

from blog.models import *

categories_dict = {
    'Размышления тренера': 'Размышления тренера',
    'Репортаж (с турниров)': 'Репортажи с событий в Екатеринбурге',
    'Репортаж - выездные турниры': 'Репортажи с выездных турниров',
    'ИТОГИ': 'Итоги',
    'Повседневное с занятий': 'Повседневное с занятий',
    'Шутки-прибаутки': 'Шутки-прибаутки',
    'Праздники': 'Праздники',
}

df = pd.read_csv('temp_data/categorized_posts.csv')


def find_title(text):
    titles = []
    for punct in ['!', '.']:
        try:
            punct = text.find(punct)
            title = text[:punct]
            titles.append(title)
        except:
            continue

    if len(titles) > 1:
        if len(titles[0]) > len(titles[1]):
            title = titles[1]
        else:
            title = titles[0]
    else:
        title = titles[0]

    if len(title) > 70:
        title = title[:70] + '...'

    return title


def add_images(post, post_id):
    images_dir = f"temp_data/photos/{post_id}/"
    images_names = [f for f in listdir(images_dir)]

    if not images_names:
        post.delete()

        return False

    for name in images_names:
        new_name = str(post_id) + '_' + name
        copyfile(images_dir + name, os.path.dirname(os.path.dirname(os.getcwd())) + '/media/' + new_name)

        image = PostImage.objects.create(
            post=post,
            image='/media/' + new_name
        )

        image.save()

        if not post.image:
            post.image = '/media/' + new_name
            post.save()


def start_import():
    for i in range(len(df)):
        print(df['post_id'][i], df['category'][i], df['date'][i])
        category = categories_dict[df['category'][i]]
        db_category = Category.objects.get(title=category)

        post_id = df['post_id'][i]

        text = df['text'][i]
        text_list = []
        if text:
            if '\n' in str(text):
                for row in text.split("\n"):
                    text_list.append("<p>" + row.replace('\n', '') + "</p>")
            else:
                text = text
        else:
            text = ''
        db_text = ''.join(text_list)
        title = find_title(db_text).replace('<p>', '').replace("</p>", '')
        print(title)

        post = Post.objects.create(
            title=title,
            text = db_text,
            category = db_category,
            published_date=df['date'][i]
        )

        add_images(post, post_id)

        # post.save()


start_import()


