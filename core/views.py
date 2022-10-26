from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Campeao, Regiao, Funcao
from .serializers import CampeaoSerializer, RegiaoSerializer, FuncaoSerializer


def index(request):
    campeoes = Campeao.objects.all()

    context = {
        'campeoes': campeoes
    }
    return render(request, 'index.html', context)


def campeao(request, pk):
    campe = get_object_or_404(Campeao, id=pk)

    context = {
        'campeao': campe
    }
    return render(request, 'personagem.html', context)


class CampeoesView(generics.ListAPIView):
    queryset = Campeao.objects.all()
    serializer_class = CampeaoSerializer

    def get_queryset(self):
        if self.kwargs.get('regiao_pk'):
            return self.queryset.filter(regiao_id=self.kwargs.get('regiao_pk'))
        elif self.kwargs.get('funcao_pk'):
            return self.queryset.filter(funcao_id=self.kwargs.get('funcao_pk'))
        return self.queryset.all()


class CampeaoView(generics.RetrieveAPIView):
    queryset = Campeao.objects.all()
    serializer_class = CampeaoSerializer

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


class RegioesView(generics.ListAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


class RegiaoView(generics.RetrieveAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


class FuncoesView(generics.ListAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer


class FuncaoView(generics.RetrieveAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

