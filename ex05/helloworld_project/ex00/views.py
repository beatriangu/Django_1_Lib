# helloworld/views.py

# from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse("Hello World!")

from django.http import HttpResponse


def helloworld(request):
    return HttpResponse("Hello, world!")