from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.urls import reverse
from django.shortcuts import render
from decouple import config
import requests

from covidData_app.models import Country
from covidData_app.api.serializers import CountrySerializer
from covidData_app.api.pagination import CountryListPagination

class CountryListView(generics.ListAPIView):
    '''
    ListAPIView for get requests for countries, 
    create only allowed through the admin panel.
    '''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id','name', 'created','updated', 'confirmed', 'critical', 'deaths', 'recovered']
    ordering = ['-updated']


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    RetrieveUpdateDestroyAPIView for get,post and delete requests for a specific country.
    '''
    serializer_class = CountrySerializer

    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            return Country.objects.filter(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CountryDetailFilterView(generics.ListAPIView):
    '''
    Filter according to fixed country codes available,
    needs an exact match to retrieve data.
    Searches accoring to country name.
    Ordering based on the mentioned fields
    '''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'created','updated', 'confirmed', 'critical', 'deaths', 'recovered']
    ordering = ['updated']
    search_fields = ['name']
    filterset_fields = ['code']
    pagination_class = CountryListPagination


@api_view(['GET'])
def CountryDataFetchView(request, **kwargs):
    '''
    view for retrieving data from rapidAPI and serializing it and storing in db
    '''
    query_url = config('RAPID_API_QUERY_URL')

    headers = {
    'x-rapidapi-host': config('RAPID_API_HOST'),
    'x-rapidapi-key': config('RAPID_API_KEY')
    }

    if request.method == 'GET':
        code = request.GET.get('code', None)
        if code is not None:
            querystring = {"code":code}
            queryset = Country.objects.filter(code=code.upper()).exists()
            if queryset != True:
                response = requests.request("GET", query_url, headers=headers, params=querystring).json()
            else:
                return Response({"response":"Country Already exists!"},status=status.HTTP_400_BAD_REQUEST)
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


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)