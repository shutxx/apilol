from django.contrib import admin

from .models import Campeao, Regiao, Funcao


@admin.register(Campeao)
class CampeaoAdmin(admin.ModelAdmin):
    list_display = ('campeao', 'funcao', 'lore', 'regiao', 'passiva', 'descricaopassiva', 'skillq', 'descricaoskillq',
                    'skillw', 'descricaoskillw', 'skille', 'descricaoskille', 'skillr', 'descricaoskillr', 'foto')


@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('nomeregiao', 'lore_regiao', 'fotoregiao')


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ['funcao']
