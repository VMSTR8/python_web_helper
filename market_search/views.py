from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from market_search.serializer import *
from market_search.filter import *

from .models import Items


# Homepage
def index(request):
    return HttpResponse('Blank page')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ItemsFilter(self.request.GET, queryset=self.get_queryset())
        return context


# Endpoint
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dbwrite(request):
    serializer = DatabaseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
