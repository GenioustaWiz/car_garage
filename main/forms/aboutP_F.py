from django import forms
from tinymce.widgets import TinyMCE
from ..models.aboutP_M import AboutPage, AboutList

class AboutPageForm(forms.ModelForm):
    body =  forms.CharField(widget=TinyMCE ()) #tinymce Editor.
    class Meta:
        model = AboutPage
        fields = ['heading', 'body']

class AboutListForm(forms.ModelForm):
    class Meta:
        model = AboutList
        fields = ['title', 'image', 'desc']
