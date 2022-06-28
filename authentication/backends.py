#handles the backend login stuff and all

import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

#JWT Token authentication
class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request) #get the header

        #no data then dont check
        if not auth_data:
            return None

        #request comes in form of a bearer prefix in the header
        prefix, token = auth_data.decode('utf-8').split(' ') #convert from the byte to the string format and split

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithm='HS256') #authenticate the token
            user = User.objects.get(username=payload['username'])
            return (user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Invalid Token. Authentication Failed!') #invalid token
        
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Token Expired. Authentication Failed!') #expired token

        return super().authenticate(request)

