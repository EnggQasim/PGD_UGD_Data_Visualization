from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("<h1>Pakistan zinda bad</h1>")