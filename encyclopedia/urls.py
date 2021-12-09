from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.article, name="article"),
    path("new_article/", views.create, name="create"),
    path("search_results/", views.search, name="search"),
    path("rando/", views.rando, name="rando"),
    path("edit_choice/", views.select_article_for_edit, name="choice"),
]
