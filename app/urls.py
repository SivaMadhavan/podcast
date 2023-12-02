from django.urls import path
from .views import *

urlpatterns = [
    path('', PodcastCreateView.as_view()),
    path('list', PodcastListView.as_view()),
    path('<podcastId>/episode', EpisodeCreateView.as_view()),
    path('<podcastId>/episode/list', EpisodeListView.as_view()),
    path('<podcastId>/episode/<episodeId>', EpisodeReadView.as_view()),
    path('<podcastId>/episode/<episodeId>', EpisodeDeleteView.as_view())
]
