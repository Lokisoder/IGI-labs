from rest_framework import serializers

from core.helpers import create_meta
from ..models import EmployeePosition


class EmployeePositionSerializer(serializers.ModelSerializer):
    Meta = create_meta(EmployeePosition)
