from django import forms
from stock.models import Item
from django.forms import SelectMultiple, CheckboxSelectMultiple
from .models import PrinterModel


class AddPrinterModelForm(forms.ModelForm):
    ink_list = Item.objects.filter(category__name__icontains="ink")
    ink = forms.ModelMultipleChoiceField(queryset=ink_list, widget=CheckboxSelectMultiple)


    class Meta:
        model = PrinterModel
        fields = ['name', 'manufacturer', 'ink', 'colour_printer']
       
