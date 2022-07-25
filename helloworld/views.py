from django.http import HttpResponse

def index(request):
    message = request.GET.get('parameter')
    return HttpResponse("Hello, world!")
