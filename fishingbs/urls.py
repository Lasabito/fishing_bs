from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fishingbs.main.urls')),
    path('profile/', include('fishingbs.accounts.urls')),
    path('weather/', include('fishingbs.weather.urls')),
    path('news/', include('fishingbs.news.urls')),
    path('fishing-areas/', include('fishingbs.areas.urls')),
    path('weather-warnings/', include('fishingbs.weather_warnings.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
