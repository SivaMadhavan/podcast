from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_swagger_view(title='Pastebin API')

API_VERSION = settings.API_VERSION

urlpatterns = [
    path(r'', schema_view),
    path('admin/', admin.site.urls),
    path('api/' + API_VERSION + '/podcasts/', include('app.urls')),
    path('api/' + API_VERSION + '/auth/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
