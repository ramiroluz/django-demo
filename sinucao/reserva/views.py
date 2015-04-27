from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from .models import Cliente, Mesa, Reserva

def index(request):
    template = loader.get_template('reservas/index.html')
    context = RequestContext(request, {
        'mensagem': 'Bem vindo ao Sinucão',
    })
    return HttpResponse(template.render(context))

#def index(request):
#    return HttpResponse('Bem vindo ao Sinucão')


class ListaView(generic.ListView):
    template_name = 'reservas/lista.html'
    context_object_name = 'lista_clientes'

    def get_queryset(self):
        return Cliente.objects.order_by('-data_registro')[:5]


class ClienteView(generic.DetailView):
    model = Cliente
    template_name = 'reservas/cliente.html'


class ReservaView(generic.DetailView):
    model = Reserva
    template_name = 'reservas/reserva.html'

