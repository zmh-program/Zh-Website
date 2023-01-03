from django.conf.urls import url
from django.urls import path
from .views import *
from .search_views import BlogSearchView


urlpatterns = [
    path("", index, name="index"),
    path("article/<int:idx>/", article, name="article"),
    path("submit/like/<int:idx>/", like, name="like"),
    url(r'^search/', BlogSearchView(), name="haystack_search"),
]