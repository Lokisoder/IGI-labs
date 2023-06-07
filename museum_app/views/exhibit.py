from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from ..filters import ExhibitFilterSet
from ..models import Exhibit
from ..serializers import ExhibitSerializer
from ..services import ExhibitService


class ExhibitViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['title']
    filterset_class = ExhibitFilterSet

    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer

    @action(methods=['get'], detail=False)
    def recent(self, request):
        exhibits = ExhibitService.get_recent_exhibits()
        serializer = ExhibitSerializer(exhibits, many=True)
        return Response(serializer.data)
