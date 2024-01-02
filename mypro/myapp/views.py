from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes,permission_classes, api_view
from rest_framework. authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        serilizer = UserSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse({"status": "success", "message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"status": "fail", "message": serilizer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, User)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"status": "success", "message": "User Logged In Successfully", "token": token.key}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "fail", "message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    if request.method == "GET":
        user = request.user
        serializer = UserSerializer(User)
        return Response(serializer.data)