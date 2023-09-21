from time import sleep
from django import forms
from apps.resources.models import Tag


# try:
#     print("BEFORE TESTING")
#     sleep(5)
#     tags = Tag.objects.all()[0].id
#
# except Exception as err:
#     print("ERROR: ", err)
#     pass


def get_tags():
    options = ((tag.id, tag.name) for tag in Tag.objects.all())
    return options


class PostResourceForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    link = forms.URLField(widget=forms.TextInput(attrs={'class': 'field'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'field'}), )

    tags = forms.MultipleChoiceField(choices=get_tags, widget=forms.CheckboxSelectMultiple)
