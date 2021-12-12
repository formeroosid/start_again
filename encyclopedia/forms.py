from django import forms
from .util import list_entries


class SearchForm(forms.Form):
    entry = forms.CharField(label='', widget=forms.TextInput(attrs={'required': False}))

class NewArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 60, 'rows': 3, 'required': True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5, 'required': True}))

class EditArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 60, 'rows': 3, 'Field.disabled' : True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5, 'required': True}))

    # def __init__(self, data, **kwargs):
        # inital = kwargs.get('initial', {})
        # data = {**inital, **data}

