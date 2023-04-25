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
        }
        labels = {
            "printer": "",
        }


class PrinterUnAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = PrinterAssignment
        fields = "__all__"
        widgets = {
            "printer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "employee": HiddenInput(),
            "date_assigned": HiddenInput(),
            "dept": HiddenInput(),
            "unit_section": HiddenInput(),
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
        }
        labels = {
            "computer": "",
        }


class ComputerUnAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerAssignment
        fields = "__all__"
        widgets = {
            "computer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "employee": HiddenInput(),
            "date_assigned": HiddenInput(),
        }
        labels = {
            "computer": "",
        }