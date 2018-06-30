from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bet_id>', views.bet, name='bet')
]
