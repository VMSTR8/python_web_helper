from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from market_search.serializer import ItemsSerializer
from market_search.filter import *

from market_search.models import Items


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


@csrf_exempt
def write_to_db(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemsSerializer(data=data)
        print(data)
        if serializer.is_valid():
            instance, created = Items.objects.update_or_create(
                item_name=serializer.validated_data.get('item_name', None),
                defaults=serializer.validated_data
            )
            if not created:
                serializer.update(instance, serializer.validated_data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    else:
        return HttpResponseNotAllowed('Method Not Allowed')
