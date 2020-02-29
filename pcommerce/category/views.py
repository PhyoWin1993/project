from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"category/index.html",{"title":"HOME PAGE"})

def about(request):
    return render(request,"category/about.html",{"title":"ABOUT PAGE"})

