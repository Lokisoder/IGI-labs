from rest_framework import serializers

from core.helpers import create_meta
from ..models import Exhibit


class ExhibitSerializer(serializers.ModelSerializer):
    Meta = create_meta(Exhibit)
