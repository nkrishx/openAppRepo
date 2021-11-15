from django.urls import path
from covidData_app.api.views import CountryListView, CountryDetailView, CountryDetailFilterView, CountryDataFetchView

 
urlpatterns = [ 
    path('', CountryListView.as_view(), name='country-list'),
    path('country/fetch/', CountryDataFetchView, name='country-fetch'),
    path('country/', CountryDetailFilterView.as_view(), name='country-filter-detail'),
    path('country/data/', CountryListView.as_view(), name='country-list'),
    path('country/data/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
]