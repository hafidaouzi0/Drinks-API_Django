#this will describe the process of going from python object to json
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    #we gonna have an inner class Meta
    #where we gonna have the metadata describing the model
    class Meta:
        model=Drink
        fields=["id","name","description"]
        #we gonna need the serializer when we try to return our model through our api
        #we have our model , we have our serializer , now we create our endpoints