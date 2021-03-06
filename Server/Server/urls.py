"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from GGuide import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('game/', views.game_views, name='game'),
    path('blog/', views.blog_views, name='blog'),
    path('login/', views.log_in, name='login'),
    path('profile/', views.profile_user, name='profile'),
    path('friend/', views.friend_list, name='friend'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('remove_friend/', views.remove_friend, name='remove_friend'),
    path('logout/', LogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('changeinfo/', views.change_info, name='changeinfo'),
    path('articles/', views.articles, name="articles"),
    path('articles/create/', views.article_create, name="create_article"),
    path('cube_slam/', views.cube_slam, name="cube_slam"),
    path('hexgl/', views.hexgl, name="hexgl"),
    path('your_articles/', views.profile_user_articles, name="profile_articles"),
    path('gridgarden/', views.gridgarden, name="gridgarden"),
    path('articles/<slug>/', views.article_detail, name='detail'),
    path('<slug>/like/', views.article_likes, name='like-toggle'),
    path('comments/<id>/likes/', views.comment_likes, name='comment_likes'),
    path('article/<slug>/remove/', views.article_remove, name='remove_article'),
    path('comments/<id>/remove/', views.comment_remove, name='comment_remove'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
