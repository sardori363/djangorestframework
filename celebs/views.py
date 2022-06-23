from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CelebsSerializer
from .models import Celebs

class CelebsViewSet(viewsets.ModelViewSet):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer

# class CelebsAPIList(generics.ListCreateAPIView):
#     queryset = Celebs.objects.all()
#     serializer_class = CelebsSerializer
#
# class CelebsAPIUpdate(generics.UpdateAPIView):
#     queryset = Celebs.objects.all()
#     serializer_class = CelebsSerializer
#
# class CelebsDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Celebs.objects.all()
#     serializer_class = CelebsSerializer

