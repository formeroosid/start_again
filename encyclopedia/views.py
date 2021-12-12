from django.shortcuts import render
from .forms import SearchForm, NewArticleForm, EditArticleForm
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def article(request, title):
    return render(request, "encyclopedia/article.html", {
        "title": util.markup_to_html(title)
    })


def rando(request):
    entry_list = util.list_entries()
    rand = random.choice(entry_list)
    return render(request, "encyclopedia/rando.html", {
        "title": util.markup_to_html(rand)
    })


def create(request):
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
    return render(request, "encyclopedia/new_article.html", {'form1': form})


def search(request):
    keywords = request.GET.getlist('entry')
    results = None
    if len(keywords) > 0:
        results = util.search_entry(keywords[0])
    return render(request, "encyclopedia/search_results.html", {'results': results})



def edit_article(request, title):
    form = EditArticleForm()
    entry_data = util.edit_entry(title)

    return render(request, "encyclopedia/edit_article.html", {"form2": form, "file": f})



