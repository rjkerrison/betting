from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bet_id>', views.bet, name='bet'),
    path('<int:bet_id>.json', views.bet_json, name='betjson'),
]
