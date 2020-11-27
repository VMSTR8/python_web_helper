from django.urls import path
from django.conf.urls import url

from .views import *
from market_search import views

urlpatterns = [
    path('search/', search),
    path('search/result/', SearchResultView.as_view(), name='search_result'),

    url(r'^dbwrite/$', views.dbwrite),
]
