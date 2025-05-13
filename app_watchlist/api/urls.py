from django.urls import path
from app_watchlist.api import views

urlpatterns = [
    path("list/", views.MovieListAV.as_view(), name="movie_list"),
    path("<int:pk>/", views.MovieDetailAV.as_view(), name="movie_detail"),
    # path("list/", views.movie_list, name="movie_list"),
    # path("<int:pk>/", views.movie_detail, name="movie_detail"),
]
