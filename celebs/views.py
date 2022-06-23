from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CelebsSerializer
from .models import Celebs


class CelebsAPIList(generics.ListCreateAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer

class CelebsAPIUpdate(generics.UpdateAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer

class CelebsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer

# class CelebsAPIView(APIView):
#     def get(self, request):
#         w = Celebs.objects.all()
#         return Response({'posts': CelebsSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = CelebsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # save() method i serializers da yozgan create() methodimizni ozi chaqirib validate qilgan datamizni verib yuboradi.
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Celebs.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesn't exist"})
#
#         serializer = CelebsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         Celebs.objects.get(pk=pk).delete()
#         return Response({"post" :"deleted post " + str(pk)})
