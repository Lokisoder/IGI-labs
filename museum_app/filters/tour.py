import django_filters

SEASON_CHOICES = (
    (0, 'winter'),
    (1, 'spring'),
    (2, 'summer'),
    (3, 'fall'),
)


class TourFilterSet(django_filters.FilterSet):
    season = django_filters.ChoiceFilter(method='season_filter', label='Filter by season')

    def season_filter(self, queryset, field_name, value):
        if value:
            return queryset.filter(hall__floor=value)

        return queryset
