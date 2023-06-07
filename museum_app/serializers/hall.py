from rest_framework import serializers

from core.helpers import create_meta
from ..models import Hall


class HallSerializer(serializers.ModelSerializer):
    area = serializers.FloatField(min_value=0)

    Meta = create_meta(Hall)
