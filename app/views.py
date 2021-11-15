from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def love(request):
    return HttpResponse('<h1>happy love day</h1>')

def dhoni(request):
    return HttpResponse('<marquee>dhoni is the best palyer</marquee>')

def rohit(request):
    return HttpResponse('rohit is hitman')
