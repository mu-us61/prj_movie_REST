from django.urls import path
from app_watchlist.api import views

urlpatterns = [
    path("list/", views.WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>/", views.WatchDetailAV.as_view(), name="movie_detail"),
    path("stream/", views.StreamPlatformAV.as_view(), name="stream_list"),
    path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(), name="stream_detail"),
    # path("review/", views.ReviewList.as_view(), name="review_list"),
    # path("review/<int:pk>", views.ReviewDetail.as_view(), name="review_detail"),
    path("stream/<int:pk>/review/", views.ReviewList.as_view(), name="review_list"),  # film x e ait reviewlar  listesi
    path("stream/review/<int:pk>", views.ReviewDetail.as_view(), name="review_detail"),  # review ijn kendi idsi
]
