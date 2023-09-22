from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Podcast, Episode, UpVotes
from .serializers import *
from rest_framework.pagination import PageNumberPagination


class PodcastCreateView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        response = Podcast().create(request, *args, **kwargs)
        return Response(response, HTTP_201_CREATED)


class PodcastListView(ListAPIView):
    serializer_class = PodcastListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Podcast().list()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class PodcastDeleteView():
    authentication_classes = (TokenAuthentication,)

    def get(self, *args, **kwargs):
        response = {}
        return Response(response, HTTP_204_NO_CONTENT)


class EpisodeCreateView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        response = Episode().create(request, *args, **kwargs)
        return Response(response, HTTP_201_CREATED)


class EpisodeListView(ListAPIView):
    serializer_class = EpisodeListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Episode().list(**self.kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EpisodeReadView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        response = {}
        return Response(response, HTTP_200_OK)


class EpisodeDeleteView(APIView):
    authentication_classes = (TokenAuthentication,)

    def delete(self, *args, **kwargs):
        response = {}
        return Response(response, HTTP_204_NO_CONTENT)
