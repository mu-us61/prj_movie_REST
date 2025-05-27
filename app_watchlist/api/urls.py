from django.urls import path, include
from app_watchlist.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("stream", views.StreamPlatformVS, basename="stream_platform")

urlpatterns = [
    path("", include(router.urls)),
    path("list/", views.WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>/", views.WatchDetailAV.as_view(), name="movie_detail"),
    path("<int:pk>/review/", views.ReviewList.as_view(), name="review_list"),  # film x e ait reviewlar  listesi
    path("review/<int:pk>/", views.ReviewDetail.as_view(), name="review_detail"),  # review icin kendi idsi
]
