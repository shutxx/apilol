from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Campeao, Regiao, Funcao
from .serializers import CampeaoSerializer, RegiaoSerializer, FuncaoSerializer

"""
FUNÇÕES DOS TEMPLATES
"""


def index(request):
    func = Funcao.objects.all()

    context = {
        'funcoes': func
    }
    return render(request, 'index.html', context)


# Regiões de runettera
def regioes(request):
    regi = Regiao.objects.all()
    func = Funcao.objects.all()

    context = {
        'regioes': regi,
        'funcoes': func
    }
    return render(request, 'regioes.html', context)


# Região específica de runeterra
def regiao(request, pk):
    regia = get_object_or_404(Regiao, id=pk)
    camp = Campeao.objects.all()
    func = Funcao.objects.all()

    context = {
        'regiao': regia,
        'campeoes': camp,
        'funcoes': func
    }
    return render(request, 'regiao.html', context)


# Todos os campeões do jogo
def todos(request):
    campeoes = Campeao.objects.all()
    func = Funcao.objects.all()

    context = {
        'campeoes': campeoes,
        'funcoes': func
    }
    return render(request, 'todos.html', context)


# Um campeão específico
def campeao(request, pk):
    campe = get_object_or_404(Campeao, id=pk)
    func = Funcao.objects.all()
    regi = Regiao.objects.all()

    context = {
        'campeao': campe,
        'funcoes': func,
        'regioes': regi
    }
    return render(request, 'personagem.html', context)


def funcao(request, pk):
    func = Funcao.objects.all()
    funca = get_object_or_404(Funcao, id=pk)
    campeoes = Campeao.objects.all()

    context = {
        'funcoes': func,
        'funcao': funca,
        'campeoes': campeoes,

    }
    return render(request, 'funcao.html', context)


"""
VIEWS DA API
"""


# Views da api mostrar todos os campeões
class CampeoesView(generics.ListAPIView):
    queryset = Campeao.objects.all()
    serializer_class = CampeaoSerializer

    # Buscando campeoes específico de cada região ou função
    def get_queryset(self):
        if self.kwargs.get('regiao_pk'):
            return self.queryset.filter(regiao_id=self.kwargs.get('regiao_pk'))
        elif self.kwargs.get('funcao_pk'):
            return self.queryset.filter(funcao_id=self.kwargs.get('funcao_pk'))
        return self.queryset.all()


# Views da api para um campeao especifico
class CampeaoView(generics.RetrieveAPIView):
    queryset = Campeao.objects.all()
    serializer_class = CampeaoSerializer

    # pegando um campeao especifico de cada região ou função
    def get_object(self):
        if self.kwargs.get('regiao_pk'):
            return get_object_or_404(self.get_queryset(),
                                     regiao_id=self.kwargs.get('regiao_pk'),
                                     pk=self.kwargs.get('campeao_pk'))
        elif self.kwargs.get('funcao_pk'):
            return get_object_or_404(self.get_queryset(),
                                     funcao_id=self.kwargs.get('funcao_pk'),
                                     pk=self.kwargs.get('campeao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('campeao_pk'))


# View para pegar todas as regioes
class RegioesView(generics.ListAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


# View para pegar uma região específica
class RegiaoView(generics.RetrieveAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


# View para pegar todas as funções
class FuncoesView(generics.ListAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer


# View para pegar uma função específica
class FuncaoView(generics.RetrieveAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
