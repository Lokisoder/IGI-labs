from rest_framework import viewsets, permissions

from ..models import Hall
from ..serializers import HallSerializer


class HallViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    queryset = Hall.objects.all()
    serializer_class = HallSerializer
