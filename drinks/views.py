#this is where we create all our endpoints
#an endpoint is a certain url you can access data from

from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def list_drinks(request):

 if request.method == 'GET':
    #get all the drinks
    drinks=Drink.objects.all()
    #serialize them
    serializer= DrinkSerializer(drinks,many=True)
    #return json
    return Response(serializer.data)

 if request.method == 'POST':
    #add a drink to the db: is a similar procss in the opposite way
    #take the sent data
    #deserialize the data
    #create drink object out of it
    serializer=DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
     drink= Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
      serializer=DrinkSerializer(drink)
      return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
