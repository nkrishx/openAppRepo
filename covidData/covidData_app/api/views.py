from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
import requests

from covidData_app.models import Country
from covidData_app.api.serializers import CountrySerializer
from covidData_app.api.pagination import CountryListPagination

class CountryListView(generics.ListAPIView):
    '''
    ListAPIView for get and post requests for countries, 
    create only allowed through the admin panel.
    '''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
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


@api_view(['GET'])
def CountryDataFetchView(request):
    query_url = "https://covid-19-data.p.rapidapi.com/country/code"

    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "3ad19a4761msh51ac800fb2e2c5ap159813jsne62cfb3dca3c"
    }

    if request.method == 'GET':
        code = request.GET.get('code', None)
        if code is not None:
            querystring = {"code":code}
            response = requests.request("GET", query_url, headers=headers, params=querystring).json()
            if len(response)!=0:
                serializer = CountrySerializer(data=response[0])
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        