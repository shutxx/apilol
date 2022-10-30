from rest_framework import serializers

from core.models import Campeao, Regiao, Funcao


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = [
            'id',
            'funcao',
        ]


class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = [
            'id',
            'nomeregiao',
            'lore_regiao',
            'fotoregiao',
        ]


class CampeaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeao
        fields = [
            'id',
            'campeao',
            'funcao',
            'lore',
            'regiao',
            'passiva',
            'descricaopassiva',
            'skillq',
            'descricaoskillq',
            'skillw',
            'descricaoskillw',
            'skille',
            'descricaoskille',
            'skillr',
            'descricaoskillr',
            'descricao',
            'foto',
        ]
