from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def test(request):
    return Response({
        'msg':"Test is working!",
        'status': status.HTTP_200_OK
    })
