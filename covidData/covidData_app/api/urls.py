from django.urls import path
from covidData_app.api.views import CountryList, CountryDetail

 
urlpatterns = [ 
    path('', CountryList.as_view(), name='country-list'),
    #path('country/', CountryDetailFilterView.as_view(), name='country-filter-detail'),
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
]