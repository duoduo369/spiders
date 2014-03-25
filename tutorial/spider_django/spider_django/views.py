# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from rest_framework import authentication, exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from myauth.models import User
from myauth.serializers import UserSerializer


class Login(APIView):

    permission_classes = (AllowAny, )

    def get_param(self, request):
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        return username, password

    def get(self, request):
        username, password = self.get_param(request)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response()
        else:
            raise exceptions.AuthenticationFailed()

class Logout(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        logout(request)
        return Response()

class UserDetail(APIView):

    def get(self, request):
        seri = UserSerializer(request.user)
        return Response(seri.data)

class TestApi(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        return Response()

class Register(APIView):

    permission_classes = (AllowAny,)

    def get_param(self, request):
        username = request.DATA.get('username', '')
        email = request.DATA.get('email', '')
        password = request.DATA.get('password', '')

        return username, email, password

    def post(self, request):
        username, email, password = self.get_param(request)
        user = User.objects.create_user(username, email, password)
        return Response()
