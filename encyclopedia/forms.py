from django import forms
from .util import list_entries


class NewArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 60, 'rows': 3, 'required': True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5, 'required': True}))

class EditArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 60, 'rows': 3, 'Field.disabled' : True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5, 'required': True}))

class ChooseArticleForEdit(forms.Form):
    entries = list_entries()
    file_names = [(file_name, file_name) for file_name in entries]
    article = forms.CharField(label="Choose the article you would like to edit.", widget=forms.Select(choices=file_names))

