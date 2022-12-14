from django.urls import path

from .views import CampeaoView, CampeoesView, RegiaoView, RegioesView, FuncaoView, FuncoesView


urlpatterns = [
    path('campeoes/', CampeoesView.as_view(), name='campeoes'),
    path('campeoes/<int:campeao_pk>/', CampeaoView.as_view(), name='campeao'),
    path('campeoes/<int:campeao_pk>/regiao', RegiaoView.as_view(), name='campeao_regiao'),

    path('regioes/', RegioesView.as_view(), name='regioes'),
    path('regioes/<int:pk>/', RegiaoView.as_view(), name='regiao'),
    path('regioes/<int:regiao_pk>/campeoes/', CampeoesView.as_view(), name='regioes_campeoes'),
    path('regioes/<int:regiao_pk>/campeoes/<int:campeao_pk>/', CampeaoView.as_view(), name='regiao_campeao'),

    path('funcoes/', FuncoesView.as_view(), name='funcoes'),
    path('funcoes/<int:pk>/', FuncaoView.as_view(), name='funcao'),
    path('funcoes/<int:funcao_pk>/campeoes/', CampeoesView.as_view(), name='funcoes_campeoes'),
    path('funcoes/<int:funcao_pk>/campeoes/<int:campeao_pk>/', CampeaoView.as_view(), name='funcoes_campeoes'),
]