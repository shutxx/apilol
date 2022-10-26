from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

import core.views
from core.views import index, campeao

urlpatterns = [
    path('', index, name='index'),
    path('personagem/<int:pk>', campeao, name='personagem'),

    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
