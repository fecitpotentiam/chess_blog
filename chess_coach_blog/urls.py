"""chess_coach_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('chess_coach_blog/', include('chess_coach_blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/search/', views.search, name='search'),
    path('blog/category/<int:pk>/', views.category_post_list, name='category_post_list'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('events', views.events_list, name='events_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),

    path('albums', views.get_albums, name='get_albums'),
    path('album/<int:pk>', views.get_photos_in_album, name='get_photos_in_album'),

    path('videolessons', views.youtube_videos, name='youtube_videos'),

    path('tinymce/', include('tinymce.urls')),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
