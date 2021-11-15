from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils.timezone import make_aware
import datetime
from decouple import config

from covidData_app.models import Country
from covidData_app.api.serializers import CountrySerializer


class CountryListViewTestcase(APITestCase):
    '''
    test case to check if we can retrieve and display all country objects
    '''
    def test_country_list(self):
        response = self.client.get(reverse('country-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CountryDetailFilterViewTestcase(APITestCase):
    '''
    test case to check if we can retrieve and display all country objects 
    based of the filtering, ordering and search setup for the view
    '''
    def test_country_list(self):
        response = self.client.get(reverse('country-filter-detail'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CountryDetailViewTestCase(APITestCase):
    '''
    test cases for checking an individual country object and 
    allowed operations on it
    '''
    def setUp(self):
        self.country = Country.objects.create(country="Test Country", 
            code="TC",
            confirmed=100,
            recovered=100,
            critical=10,
            deaths=10,
            latitude=12.10,
            longitude=10.50,
            lastChange=make_aware(datetime.datetime.today()),
            lastUpdate=make_aware(datetime.datetime.today()))

    def test_country_detail_individual_get(self):
        response = self.client.get(reverse('country-detail', args=(self.country.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_detail_individual_delete(self):
        response = self.client.delete(reverse('country-detail', args=(self.country.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_country_detail_individual_update(self):
        data = {
            "country": "Test Country",
            "code": "TC",
            "confirmed": 200,
            "recovered": 100,
            "critical": 10,
            "deaths": 10,
            "latitude": 12.10,
            "longitude": 10.50,
            "lastChnage": make_aware(datetime.datetime.today()),
            "lastUpdate": make_aware(datetime.datetime.today())
        }

        response = self.client.patch(reverse('country-detail', args=(self.country.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CountryDataFetchViewTestCase(APITestCase):
    '''
    Test case to retrieve data from rapidAPI and insert into db
    custom string generated with get
    '''
    def setUp(self):
        self.code = "IE"

    def test_country_fetch_get(self):
        response = self.client.get('%s?code=%s'%(reverse('country-fetch'), self.code))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 