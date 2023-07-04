from django import forms
from django.forms import DateInput, HiddenInput, Select

from .models import ComputerAssignment, PrinterAssignment




class PrinterAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = PrinterAssignment
        fields = "__all__"
        exclude = ["date_returned"]
        widgets = {
            "printer": HiddenInput(),
            "is_assigned": HiddenInput(),
            "date_assigned": HiddenInput(),
            
        }
        labels = {
            "printer": "",
        }


class PrinterUnAssignmentForm(forms.ModelForm):
    class Meta:
        model = PrinterAssignment
        fields = "__all__"
        widgets = {
            "printer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "employee": HiddenInput(),
            "date_assigned": HiddenInput(),
            "section": HiddenInput(),
            "is_assigned": HiddenInput(),
            
        }
        labels = {
            "printer": "",
        }


class ComputerAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerAssignment
        fields = "__all__"
        exclude = ["date_returned"]
        widgets = {
            "computer": HiddenInput(),
            "is_assigned": HiddenInput(),
            "date_assigned": HiddenInput(),
        }
        labels = {
            "computer": "",
        }


class ComputerUnAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerAssignment
        fields = "__all__"
        exclude = ["section"]
        widgets = {
            "computer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "employee": HiddenInput(),
            "date_assigned": HiddenInput(),
            "is_assigned": HiddenInput(),
        }
        labels = {
            "computer": "",
        }