import django_filters

from market_search.models import Items


class ItemsFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Items
        fields = {
            'price': ['lt', 'gt']
        }
