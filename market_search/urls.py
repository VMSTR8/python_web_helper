from django.urls import path

from market_search.views import *

urlpatterns = [
    path('search/', search),
    path('search/result/', SearchResultView.as_view(), name='search_result'),

    path('dbwrite/', write_to_db)
]
