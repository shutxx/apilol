from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Campeao, Regiao, Funcao
from .serializers import CampeaoSerializer, RegiaoSerializer, FuncaoSerializer


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
        if self.kwargs.get('campeao_pk'):
            return get_object_or_404(self.get_queryset(),
                                     campeao_id=self.kwargs.get('campeao_pk'),
                                     regiao_id=self.kwargs.get('regiao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('regiao_pk'))


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