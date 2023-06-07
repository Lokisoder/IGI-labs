from rest_framework import serializers

from core.helpers import create_meta
from ..models import Tour


class TourSerializer(serializers.ModelSerializer):
    Meta = create_meta(Tour)
