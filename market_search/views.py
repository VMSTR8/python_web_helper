from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from .models import *

# Create your views here.


# Homepage
def index(request):
    return HttpResponse('Привет, мир!')


# Search page
def search(request):
    return render(request, 'search.html', {'title': 'Поиск по магазинам'})


# Search results
class SearchResultView(ListView):
    model = Items
    template_name = 'search_result.html'

    # Function that implements search through parameters
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query == '':
            object_list = Items.objects.filter(Q(store_name__icontains=query) | Q(item_name__icontains=query))
            return object_list
        else:
            return None
