from rest_framework import serializers
from restapp.models import contact


class contactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = contact
        fields = ['name', 'title', 'email']
 