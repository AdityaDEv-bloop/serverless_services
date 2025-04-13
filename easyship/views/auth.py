from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from easyship.serializers.authserializer import RegisterSerializer
from django.contrib.auth import login, logout
from easyship.utils import get_tokens_for_user, ValidateUser
import json


class Signup(APIView):
    def post(self, request):
        request_body = json.loads(request.body)
        Serializer = RegisterSerializer(data=request_body['data'])
        if Serializer.is_valid():
            Serializer.create(validated_data=request_body['data'])
            return Response({"msg":"User Created","data":Serializer.data, "status":status.HTTP_201_CREATED})

        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class SignIn(APIView):
    def post(self,request):
        body = json.loads(request.body)
        email = body["data"]["email"]
        password = body["data"]["password"]
        user = ValidateUser(Email=email, Password=password)
        if user is not None:
            login(request, user=user)
            authdata = get_tokens_for_user(user=user)
            return Response({'msg': 'Login Success', **authdata}, status=status.HTTP_200_OK)

        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class SignOut(APIView):
    def get(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)