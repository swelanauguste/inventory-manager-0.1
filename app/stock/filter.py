import django_filters
from django_filters import ChoiceFilter

from .models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.ChoiceFilter(lookup_expr="iexact")

    class Meta:
        model = Item
        fields = "__all__"
