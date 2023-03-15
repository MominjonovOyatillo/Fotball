from django.urls import path
from .views import *

urlpatterns = [
    path("get-info/", get_info),
    path("get-media/", get_media),
    path("get-news/", get_news),
    path("get-shop/", get_shop),
    path("get-statistics/", get_statistics),
    path("get-player/", get_player),
    path("get-academy/", get_academy),
]