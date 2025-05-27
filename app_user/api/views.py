from rest_framework.views import APIView
from app_user.api.serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()







# class RegistrationAV(APIView):
#     def get(self, request):
#         user = User.objects.all()
#         serializer = RegistrationSerializer(user, many=True)
#         # print(serializer.data)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = User(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
