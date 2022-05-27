import django_filters

from .models import Attendence


""" Django-filter provides a simple way to filter down a queryset based on parameters a user provides. """

class AttendenceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time']