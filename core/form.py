from django import forms
from .models import Orders
from django.forms import ModelForm


class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)
