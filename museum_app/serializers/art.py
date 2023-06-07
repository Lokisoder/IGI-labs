from rest_framework import serializers

from core.helpers import create_meta
from ..models import Art


class ArtSerializer(serializers.ModelSerializer):
    Meta = create_meta(Art)
