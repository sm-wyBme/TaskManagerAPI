from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt

#register user
class RegisterView(GenericAPIView):

    serializer_class = AccountSerializer

    #post data
    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        #validate and save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#login view
class LoginView(GenericAPIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password) #check if there is a user

        #if user present generate a token
        if user:
            auth_token = jwt.encode({'username':user.username}, settings.JWT_SECRET_KEY, algorithm='HS256')

            serializer = AccountSerializer(user)

            data={
                'user': serializer.data,
                'token': auth_token,
            }

            return Response(data,status=status.HTTP_200_OK)

        #return a response
        return Response({'detail':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
