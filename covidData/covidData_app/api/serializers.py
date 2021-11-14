from rest_framework import serializers 
from covidData_app.models import Country

class CountrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Country
        fields = "__all__"

