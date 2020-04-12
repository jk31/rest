from django.http import HttpResponse

def index(request):
    number = 3
    return HttpResponse(f"TEST={number}")
