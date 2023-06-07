from rest_framework import serializers

from core.helpers import create_meta
from core.validators import phone_number_validator
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[phone_number_validator])
    Meta = create_meta(Employee)
