from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from core.views import index, todos, campeao, regioes, regiao, funcao

urlpatterns = [
    path('', index, name='index'),

    path('personagens/', todos, name='todos'),
    path('personagem/<int:pk>', campeao, name='personagem'),

    path('regioes/', regioes, name='regis'),
    path('regiao/<int:pk>', regiao, name='regi'),

    path('funcao/', funcao, name='func'),

    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
