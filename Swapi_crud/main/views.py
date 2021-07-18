from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import requests
from rest_framework.response import Response
from .serializers import PeopleSerializer
from .models import People
from rest_framework import status


#Get Request View
@api_view(['GET'])
def get_request(request):
    if request.method == 'GET':
        api_response = requests.get('https://swapi.dev/api/people')
        if api_response.status_code != 200:
            raise Exception("Api error")
        result = People.objects.all().exists()
        if result == False:
            api_data = api_response.json()['results']
            for item in api_data:
                all_people = People(name=item['name'], height=item['height'], mass=item['mass'], hair_color=item['hair_color'], skin_color=item['skin_color'],
                                    eye_color=item['eye_color'],
                                    birth_year=item['birth_year'], gender=item['gender'],
                                    homeworld=item['homeworld'], films=item['films'],
                                    species=item['species'], vehicles=item['vehicles'], starships=item['starships'], created=item['created'], edited=item['edited'], url=item['url'])
                all_people.save()
        result = People.objects.all()
        serialize = PeopleSerializer(result, many=True)
        return Response(serialize.data)

#POST Request View
@api_view(['POST'])
def post_request(request):
    if request.method == 'POST':
        serialize = PeopleSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Data added successfully'})
        return Response(serialize.errors)


#PUT Request View
@api_view(['PUT'])
def put_request(request, id=None):
    if request.method == 'PUT':
        id = request.data.get('id')
        result = People.objects.get(id=id)
        serialize = PeopleSerializer(result, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Data Updated Successfully'})
        return Response(serialize.errors)

#Delete Request View
@api_view(['DELETE'])
def delete_request(request, id):
    if request.method == 'DELETE':
        try:
            result = People.objects.get(id=id)
            result.delete()
            return Response({'msg': 'Data Deleted Successfully'})
        except:
            return Response({'msg': 'Id not exist'})
    return Response({'msg': status.HTTP_204_NO_CONTENT})
