from django.http import HttpResponse, Http404
from django.shortcuts import render
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
  try:
    bet = Bet.objects.get(id=bet_id)
  except Bet.DoesNotExist:
    raise Http404(f'Bet #{bet_id} does not exist')
  return render(
    request,
    'selector/detail.html',
    {'bet': bet})
