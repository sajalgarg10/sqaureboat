from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from users.models import User
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


def get_tokens_for_user(user):
    """
    Generates a pair of access and refresh tokens for the given user.
    """
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(access),
    }
# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    user = User.objects.filter(email = request.data["email"])[0]
    password = request.data["password"]
    if user and check_password(password , user.password):
        token = get_tokens_for_user(user)
        return Response(token  , HTTP_200_OK)
    else:
        return Response({"response":"logged failed"} , HTTP_200_OK )


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    user = User.objects.filter(email = request.data["email"])
    if user:
        return Response("user already exists",HTTP_400_BAD_REQUEST )
    
    elif request.data["user"] == "recruiter":
        User.objects.create_superuser(username= request.data["username"] ,  email= request.data["email"] , password= request.data["password"], )
        return Response("new user ia created" , HTTP_200_OK)
    
    else:
        User.objects.create_user(username= request.data["username"] ,  email= request.data["email"] , password= request.data["password"], )
        return Response({"response":"new user ia created"} , HTTP_200_OK)


    
      

