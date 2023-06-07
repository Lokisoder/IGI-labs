from rest_framework import viewsets, permissions

from ..models import Art
from ..serializers import ArtSerializer


class ArtViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    queryset = Art.objects.all()
    serializer_class = ArtSerializer
