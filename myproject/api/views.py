from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your tests here.
from .models import Item
from .serializers import ItemSerializer
import jwt
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer =  ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def getToken(request):
    data = request.data
    print(data)
    encoded_jwt = jwt.encode({"user_name": data['name'], "email":data['email']}, "JWT_SECRET_KEY", algorithm="HS256")
    return Response({"token": encoded_jwt})
