from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return HttpResponse("hello wolrd1")
def index2(request):
    return HttpResponse("helloworld2")
    
