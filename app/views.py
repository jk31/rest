from django.http import HttpResponse

def index(request):
    number = 5
    return HttpResponse(f"TEST={number}")
