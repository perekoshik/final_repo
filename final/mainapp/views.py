from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def main(request):
    # try:
    #     print(1/0)
    # except ZeroDivisionError:
    #      context={'num':'444', 'title':'blobloblo', 'description':'blablabla',}
    #      return render(request, 'mainapp/error.html', context=context)
    return render(request, 'mainapp/main.html')

def error(request):
    return render(request, 'mainapp/error.html')