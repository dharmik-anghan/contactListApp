from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.


class RegisterView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"msg": "User not found"}, status=404)

        if authenticate(username=username, password=password):
            token, created = Token.objects.update_or_create(user=user)
            if not created:
                token.delete()
                token, created = Token.objects.update_or_create(user=user)
            return Response({"msg": "Login", "token": str(token)}, status=200)
        return Response(
            {"msg": "Username or password is not valide"},
            status=status.HTTP_404_NOT_FOUND,
        )


class LogOutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        if Token.objects.exists():
            request.user.auth_token.delete()
        else:
            return Response({"msg": "User Already Logged Out"}, status=204)

        return Response({"msg": "User Logged Out"}, status=204)
