from django.urls import path
from app_watchlist.api import views

urlpatterns = [
    path("list/", views.WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>/", views.WatchDetailAV.as_view(), name="movie_detail"),
    path("stream/", views.StreamPlatformAV.as_view(), name="stream_list"),
    path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(), name="stream_detail"),
]
