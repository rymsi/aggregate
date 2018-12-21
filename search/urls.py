# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
        path('', views.search, name='index'),
        path('results/<str:search_query>', views.results, name='results'),
        path('person/<str:person_name>', views.person, name='person')       
]
