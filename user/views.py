from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests


class UserActivationView(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        content = "Account activated"
        return Response(content)

class ResetPasswordConfirmView(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/reset_password_confirm/"
        post_data = {'uid': uid, 'token': token, "new_password": "newsecret", "re_new_password": "newsecret"}
        result = requests.post(post_url, data=post_data)
        content = "Password changed"
        return Response(content)