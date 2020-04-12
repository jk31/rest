from django.http import HttpResponse

import environ
env = environ.Env()

def index(request):
    number = env("TEST")
    return HttpResponse(f"TEST={number}")
