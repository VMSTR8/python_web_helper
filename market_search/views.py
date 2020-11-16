from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.postgres.search import TrigramSimilarity

from .models import Items


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

        # object_list = Items.objects.annotate(
        #     match=TrigramSimilarity('item_name', query),
        # ).filter(match__gt=0.15).order_by('store_name', '-match', 'price').filter(in_stock=True)

        object_list = Items.objects.filter(search_vector=query).filter(in_stock=True).order_by(
            'store_name', 'price')
        return object_list
