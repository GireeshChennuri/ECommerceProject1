from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class Login:

    def check_login(self,data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return user,token
        return None  