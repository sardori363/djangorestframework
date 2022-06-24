from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import *
from .serializers import CelebsSerializer
from .models import Celebs

class CelebsAPIList(generics.ListCreateAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )

class CelebsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CelebsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebsSerializer
    permission_classes = (IsAdminOrReadOnly,)

