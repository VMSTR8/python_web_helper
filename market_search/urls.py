from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('search/', search),
    re_path(r'^search/results/$', SearchResultView.as_view(), name='search_result'),
]
