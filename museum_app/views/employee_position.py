from rest_framework import viewsets, permissions

from ..models import EmployeePosition
from ..serializers import EmployeePositionSerializer


class EmployeePositionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    queryset = EmployeePosition.objects.all()
    serializer_class = EmployeePositionSerializer
