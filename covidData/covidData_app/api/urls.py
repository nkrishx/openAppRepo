from django.urls import path
from covidData_app.api.views import CountryList, CountryDetail, CountryDetailFilterView

 
urlpatterns = [ 
    path('', CountryList.as_view(), name='country-list'),
    path('country/', CountryDetailFilterView.as_view(), name='country-filter-detail'),
    path('country/data/', CountryList.as_view(), name='country-list'),
    path('country/data/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
]