from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import JokeService


class JokeView(APIView):

    def get(self, request, format=None):
        return Response(JokeService.get_random_joke())
