from django_filters import OrderingFilter, FilterSet

from .models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'created_on': ['exact', 'lte', 'gte'],
            'modified_on': ['exact', 'lte', 'gte'],
            "id": ['exact'],
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }

    order_by = OrderingFilter(
        fields=('created_on', 'modified_on', 'email', 'first_name', 'last_name'))
