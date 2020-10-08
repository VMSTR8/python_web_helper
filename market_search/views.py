# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from .models import *

# Create your views here.


def search(request):
    return render(request, 'search.html', {'title': 'Поиск по магазинам'})


class SearchResultView(ListView):
    model = Items
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Items.objects.filter(Q(item_name__icontains=query))
        return object_list


def index(request):
    return HttpResponse('Привет, мир!')