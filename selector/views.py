from django.http import HttpResponse
from django.template import loader
from .models import Bet

def index(request):
  bet_list = Bet.objects.order_by('-id')
  template = loader.get_template('selector/index.html')
  context = {
    'bet_list': bet_list
  }
  return HttpResponse(template.render(context, request))

def bet(request, bet_id):
  bet = Bet.objects.get(id=bet_id)
  return HttpResponse(f'You\'re looking at Bet #{bet_id}<br />{bet}')
