from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, 'index.html')
    #return HttpResponse('Hello, World!')


def home(request):
    return HttpResponse('Login Page')
