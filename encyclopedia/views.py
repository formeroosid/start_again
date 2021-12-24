import random

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from . import util
from .forms import NewArticleForm, EditArticleForm


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
    x = util.get_html_data(rand)
    title = x[0]
    content = x[1]
    return render(request, "encyclopedia/rando.html", {
        "title": title,
        "content": content
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
            if save:
                messages.success(request, f'{title} saved to disc')
            else:
                messages.error(request, f'Duplicate title - "{title}", please enter a different one.')
                return redirect('index')
    return render(request, "encyclopedia/new_article.html", {'form1': form})


def search(request):
    keywords = request.GET.getlist('entry')
    results = None
    if len(keywords) > 0:
        results = util.search_entry(keywords[0])
    return render(request, "encyclopedia/search_results.html", {'results': results})


def edit_article(request):
    if 'mode' in request.POST.keys():
        title = request.POST.get('name')
        content = request.POST.get('body')
        util.update_entry(title, content)
        messages.success(request, f"{title} saved to disc")
        return redirect(f'/wiki/{title}')
    else:
        title = list(request.POST.items())
        title = title[1]
        title = title[0]
        entry_data = util.get_data(title)
        initial_data = {
            'name': title,
            'body': entry_data
            }
        form = EditArticleForm(initial=initial_data)
        return render(request, "encyclopedia/edit_article.html", {"form": form})
