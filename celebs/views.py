from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializers import CelebsSerializer
from .models import Celebs


class CelebsAPIView(APIView):
    def get(self, request):
        lst = Celebs.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        return Response({'posts': 'bla 2'})

# class CelebsAPIView(generics.ListAPIView):
#     queryset = Celebs.objects.all()
#     serializer_class = CelebsSerializer