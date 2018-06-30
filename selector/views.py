from django.http import HttpResponse
from .models import Bet

def index(request):
  bet_list = Bet.objects.order_by('-id')
  output = ', '.join(bet for bet in bet_list)
  return HttpResponse(output)

def bet(request, bet_id):
  bet = Bet.objects.get(id=bet_id)
  return HttpResponse(f'You\'re looking at Bet #{bet_id}<br />{bet}')
