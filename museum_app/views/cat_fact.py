from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import CatFactService


class CatFactView(APIView):

    def get(self, request, format=None):
        return Response(CatFactService.get_random_fact())
