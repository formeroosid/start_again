from django.shortcuts import render
from .forms import SearchForm, NewArticleForm, ChooseArticleForEdit, EditArticleForm
from . import util
import random


def index(request):
    search_form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 'search_form': search_form})


def article(request, title):
    return render(request, "encyclopedia/article.html", {
        "title": util.markup_to_html(title)
    })


def rando(request):
    search_form = SearchForm()
    entry_list = util.list_entries()
    rand = random.choice(entry_list)
    return render(request, "encyclopedia/rando.html", {
        "title": util.markup_to_html(rand),
        'search_form': search_form
    })


def create(request):
    search_form = SearchForm()
    form = NewArticleForm()
    if request.method == "POST":  # check for a submitted form
        initial_dict = {
            "name": "name",
            "body": "body"
        }
        form = NewArticleForm(request.POST, initial=initial_dict)  # Call function to save article
        if form.is_valid():
            clean = form.cleaned_data
            title = clean["name"]
            content = clean["body"]
            save = util.save_entry(title, content)  # Capture return from save function
            return render(request, "encyclopedia/new_article.html", {'form1': form, "save": save})
    return render(request, "encyclopedia/new_article.html", {'form1': form, 'search_form': search_form})


def search(request):
    search_form = SearchForm()
    return render(request, "encyclopedia/search_results.html", {'search_form': search_form})


def edit_article(request, selection):
    form = EditArticleForm()
    path = "entries/" + selection + ".md"
    f = open(path, 'w')
    return render(request, "encyclopedia/edit_article.html", {"form2": form, "file": f})


def select_article_for_edit(request):
    form = ChooseArticleForEdit()
    return render(request, "encyclopedia/edit_choice.html", {"form3": form})
