import json

from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from easyship.serializers.authserializer import LoginSerializer, RegisterSerializer
from easyship.utils import ValidateUser, get_tokens_for_user


class Signup(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        request_body = json.loads(request.body)
        serializer = RegisterSerializer(data=request_body)
        if serializer.is_valid():
            serializer.create(validated_data=request_body)
            return Response(
                {
                    "msg": "User Created",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        request_body = json.loads(request.body)
        serializer = LoginSerializer(data=request_body)
        if serializer.is_valid():
            email = request_body["email"]
            password = request_body["password"]
            user = ValidateUser(Email=email, Password=password)
            if user is not None:
                login(request, user=user)
                authdata = get_tokens_for_user(user=user)
                return Response(
                    {"msg": "Login Success", **authdata}, status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"msg": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class SignOut(APIView):
    def get(self, request):
        logout(request)
        return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)
