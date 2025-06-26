from django import forms
from .models import ItemOne

class ItemOneForm(forms.ModelForm):
    class Meta:
        model = ItemOne
        fields = ['name', 'description']