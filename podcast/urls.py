from django.contrib import admin
from django.urls import path, include

API_VERSION = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_VERSION + '/user', include('user.urls')),
    path(API_VERSION + '/podcast', include('app.urls')),
    path(API_VERSION + '/identity', include('identity.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
