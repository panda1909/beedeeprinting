from django import forms
from .models import Orders

class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)