from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('',include('main.urls',namespace='movies')),
    path('admin/', admin.site.urls),
    path('myinfo/', include('myinfo.urls')),
    path('post_detail/', include('post_detail.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
