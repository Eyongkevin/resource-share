from importlib.resources import Resource

from django import forms


class PostResourceForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    link = forms.URLField(widget=forms.TextInput(attrs={'class': 'field'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'field'}), )