from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..filters import EmployeeFloorFilterSet
from ..models import Employee
from ..serializers import EmployeeSerializer
from ..services import EmployeeService


class EmployeeSelfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        employee = EmployeeService.find_by_user(request.user)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]

    filterset_class = EmployeeFloorFilterSet
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        qs = super().get_queryset()

        floor = self.kwargs.get('floor')
        if floor and floor.isnumeric():
            qs = qs.filter(hall__floor=int(floor))

        return qs.filter()

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
