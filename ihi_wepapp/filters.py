import django_filters
from . models import *
# from django_filters import DateFilter
from django import forms




class PublicationFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name = 'published_date', lookup_expr = 'gte', label = 'Start Date', widget = forms.DateInput(attrs = {
        'type': 'date',
    }))
    end_date = django_filters.DateFilter(field_name = 'published_date', lookup_expr = 'lte', label = 'End Date', widget = forms.DateInput(attrs = {
        'type': 'date',
    }))
    title = django_filters.CharFilter(field_name = 'title', lookup_expr='icontains', label = 'Title')
    journal_name = django_filters.CharFilter(field_name = 'journal_name', lookup_expr='icontains', label = 'Journal name')
    author = django_filters.CharFilter(field_name = 'authors', lookup_expr='icontains', label = 'Author')


class ProjectsFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name = 'start_date', lookup_expr = 'gte', label = 'Start Date', widget = forms.DateInput(attrs = {
        'type': 'date',
    }))
    end_date = django_filters.DateFilter(field_name = 'end_date', lookup_expr = 'lte', label = 'End Date', widget = forms.DateInput(attrs = {
        'type': 'date',
    }))
    title = django_filters.CharFilter(field_name = 'title', lookup_expr='icontains', label = 'Title')
    funding_partner = django_filters.CharFilter(field_name = 'funding_partner', lookup_expr='icontains', label = 'Funding Partner')
    project_leader = django_filters.CharFilter(field_name = 'project_leader', lookup_expr='icontains', label = 'Project Leader')
    principal_investigator = django_filters.CharFilter(field_name = 'principal_investigator', lookup_expr='icontains', label = 'Project Investigator')
    administrator = django_filters.CharFilter(field_name = 'administrator', lookup_expr='icontains', label = 'Project Administrator')
    department = django_filters.CharFilter(field_name = 'department', lookup_expr='icontains', label = 'Department')



class StaffFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(field_name = 'first_name', lookup_expr='icontains', label = 'First name')
    last_name = django_filters.CharFilter(field_name = 'last_name', lookup_expr='icontains', label = 'Last name')
    position = django_filters.CharFilter(field_name = 'position', lookup_expr='icontains', label = 'Position')
    units = django_filters.CharFilter(field_name = 'units', lookup_expr='icontains', label = 'Unit')

    
