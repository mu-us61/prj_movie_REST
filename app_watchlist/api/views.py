from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer
from app_watchlist.models import WatchList, StreamPlatform
from rest_framework import status
from rest_framework.views import APIView


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


class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)  # TODO bu gelen obje dictionary mi
        except:
            return Response("the thing doesnt exist there anymore")

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)  # TODO bu gelen obje dictionary mi
        serializer = StreamPlatformSerializer(platform, data=request.data)  # TODO boylemi bak
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response("succesfully deleted")
