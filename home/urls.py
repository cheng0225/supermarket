from django.urls import path

from home.views import *

app_name = 'home'

urlpatterns = [
    path('things', ThingsView.as_view()),
    path('things/add', AddThings.as_view()),
    path('things/earch', SearchView.as_view()),
    path('merchants', MerchantsView.as_view()),
    path('search', SearchView.as_view()),
    path('logs', LogsView.as_view()),
    path('orders', OrdersView.as_view()),
    path('latlon', LatLon.as_view()),
]
