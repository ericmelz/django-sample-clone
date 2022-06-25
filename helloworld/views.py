from django.http import HttpResponse

def index(request):
    print(request.path)
    return HttpResponse("Hello, world!")
