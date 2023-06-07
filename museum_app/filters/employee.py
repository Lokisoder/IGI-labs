import django_filters


class EmployeeFloorFilterSet(django_filters.FilterSet):
    floor = django_filters.NumberFilter(method='hall__floor', label='Filter by floor')

    def hall__floor(self, queryset, field_name, value):
        if value:
            return queryset.filter(hall__floor=value)

        return queryset
