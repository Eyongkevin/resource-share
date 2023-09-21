from importlib.resources import Resource

from django import forms
from apps.resources.models import Tag

try:
    print("BEFORE TESTING")
    tags = Tag.objects.all()[0].id

except Exception as err:
    print("ERROR: ", err)
    pass


class PostResourceForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    link = forms.URLField(widget=forms.TextInput(attrs={'class': 'field'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'field'}), )
