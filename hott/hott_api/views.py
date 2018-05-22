from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from ipywidgets.embed import embed_minimal_html
from hott_overlays.models import Crimes
import gmaps
import os


class UserApi(generics.RetrieveAPIView, generics.CreateAPIView):
    permission_classes = ''  # IsAuthenticated??
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if not pk:
            return Response(
                UserSerializer(request.user).data, status=status.HTTP_200_OK)
        return super().retrieve(request, pk)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrimeMap(APIView):
    """Crime map view that takes in our crime data and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for crime map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Crimes.objects.all():
            temp = []
            temp.append(each.latitude)
            temp.append(each.longitude)
            locations.append(temp)

        heatmap_layer = gmaps.heatmap_layer(locations)

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)
