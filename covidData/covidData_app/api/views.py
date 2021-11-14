from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from covidData_app.models import Country
from covidData_app.api.serializers import CountrySerializer
from covidData_app.api.pagination import CountryListPagination

class CountryList(generics.ListAPIView):
    '''
    ListAPIView for get and post requests for countries, 
    create only allowed through the admin panel.
    '''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    RetrieveUpdateDestroyAPIView for get,post and delete requests for a specific country.
    '''
    serializer_class = CountrySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Country.objects.filter(pk=pk)


class CountryDetailFilterView(generics.ListCreateAPIView):
    '''
    Filter according to fixed country codes available,
    needs an exact match to retrieve data.
    Searches accoring to country name.
    Ordering based on the mentioned fields
    '''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'update', 'confirmed', 'critical', 'deaths', 'recovered']
   # ordering_fields = '__all__'
    search_fields = ['name']
    filterset_fields = ['code']
    pagination_class = CountryListPagination