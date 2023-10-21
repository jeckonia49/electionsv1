from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import AccountUserLoginSerializer, AccountUserRegisterSerializer, AccountUserSerializer
from .validations import custom_validation, validate_email, validate_password

class UserCreateApiView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = AccountUserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user  = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = AccountUserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        



class UserLogoutApiView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
class UserApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication, )
    def get(self, request):
        serializer = AccountUserSerializer(request.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
