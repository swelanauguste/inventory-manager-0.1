from django import forms
from django.forms import CheckboxSelectMultiple

from .models import Item


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        # widgets = {"category": CheckboxSelectMultiple()}
