from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def search_form(request):
    return HttpResponse('ЗАГЛУШЕЧКА')


def index(request):
    return HttpResponse('Привет, мир!')
