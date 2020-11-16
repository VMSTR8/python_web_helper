from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('search/', search),
    path('search/results/', SearchResultView.as_view(), name='search_result'),
]
