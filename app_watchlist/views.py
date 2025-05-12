from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    # print(list(movies))
    context = {"movies": list(movies.values())}
    return JsonResponse(context)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "active": movie.active,
    }
    print(data)
    return JsonResponse(data)
