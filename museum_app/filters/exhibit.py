import django_filters

from ..models import Exhibit


class ExhibitFilterSet(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Exhibit
        fields = ['created_at']
