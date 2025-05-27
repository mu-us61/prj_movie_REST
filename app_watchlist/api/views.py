from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from app_watchlist.models import WatchList, StreamPlatform, Review
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from app_watchlist.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = Review.objects.filter(watchlist=pk)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_user_dublicate_check = Review.objects.filter(watchlist=movie, review_user=review_user).exists()
        if review_user_dublicate_check:
            raise ValidationError("the user already reviewed the show")
        else:
            review = serializer.save(watchlist=movie, review_user=review_user)
            if movie.avg_rating == 0:
                # yada serializer save yapmadan once , serializer.validated_data["rating"] burdan erisilebiliyor
                movie.avg_rating = review.rating
                movie.number_rating += 1
                movie.save()
            else:
                movie.avg_rating = (movie.avg_rating * movie.number_rating + review.rating) / (movie.number_rating + 1)
                movie.number_rating += 1
                movie.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchListAV(APIView):
    def get(self, request):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response("page does not exist", status=status.HTTP_400_BAD_REQUEST)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({"message": "deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformAV(APIView):
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class StreamPlatformDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)  # TODO bu gelen obje dictionary mi
#         except:
#             return Response("the thing doesnt exist there anymore")

#         serializer = StreamPlatformSerializer(platform)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         platform = StreamPlatform.objects.get(pk=pk)  # TODO bu gelen obje dictionary mi
#         serializer = StreamPlatformSerializer(platform, data=request.data)  # TODO boylemi bak
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         platform = StreamPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response("succesfully deleted")
