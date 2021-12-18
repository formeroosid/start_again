import re
import os

import markdown2
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content and returns True for successful save. If an existing entry with the same title already exists,
    an error string is returned.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        return False
    else:
        default_storage.save(filename, ContentFile(content))
        return True


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def search_entry(search):
    """
    Searches through the current articles and returns list of the filenames of the matched articles. If search
    fails, the function returns None.
     """
    files = os.listdir("entries")
    results = []
    for x in files:
        if x.lower().startswith(search.lower()):
            results.append(x)
    if len(results) == 0:
        return None
    else:
        for count, y in enumerate(results):
            print(count, y)
            results[count] = results[count][:-3]
        return results


def edit_entry(title):
    file_html_content = markup_to_html(title)
    return title, file_html_content


def markup_to_html(title):
    html = markdown2.markdown_path(f"entries/{title}.md")
    x = markdown2.markdown(html)
    return x
