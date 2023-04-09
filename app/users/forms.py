from django import forms
from django.forms import Textarea, TextInput

from .models import Profile, User

rounded_pill_shadow = "rounded-4"
no_border = "border-0 border-bottom rounded-0"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["is_viewer", "is_admin"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user", "uid", "slug"]
        widgets = {
            "first_name": TextInput(attrs={"class": no_border}),
            "last_name": TextInput(attrs={"class": no_border}),
            "ext": TextInput(
                attrs={
                    "class": no_border,
                    "inputmode": "numeric",
                    "type": "text",
                    "pattern": "+[0-9]",
                    "placeholder": "3909",
                }
            ),
        }