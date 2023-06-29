from django.http import HttpResponse

# from django.shortcuts import render


async def say_hello(request):
    return HttpResponse("Hello playground!")
