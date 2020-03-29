import django_filters
from .models import WellGeoinfo


class WellsFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_order')

    # first_name = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    # widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = WellGeoinfo

        # fields = (
        #     'concession',
        #     'exploration_name',
        #     'app_id__app_name',
        # )
        fields = {
            'well_type': ['exact'],
            'well_status': ['exact'],
            'exploration_name': ['icontains'],
            'production_name': ['icontains'],
            'app_id__app_name': ['icontains'],


        }

    def filter_by_order(self, queryset, name, value):
        expression = 'exploration_name' if value == 'ascending' else '-exploration_name'
        return queryset.order_by(expression)


class WellsConcFilter(WellsFilter):

    # concession = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = WellGeoinfo
        fields = {
            'concession': ['exact'],
            'well_type': ['exact'],
            'well_status': ['exact'],
            'exploration_name': ['icontains'],
            'app_id__app_name': ['icontains'],
        }
