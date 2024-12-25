from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def hello(request):
    return render(request, 'MyApp/hello.html')

def dynamic_hello(request):
    context = {'name': 'Balaji'}  # Passing the name dynamically
    return render(request, 'MyApp/dynamic_hello.html', context)