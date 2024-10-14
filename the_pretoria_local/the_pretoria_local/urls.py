# the_pretoria_local/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('directory.urls')),  # Include the directory app URLs
    path('googlebc4cc8e1dbd0d0cd.html', TemplateView.as_view(
        template_name="directory/google_verification/googlebc4cc8e1dbd0d0cd.html",
        content_type='text/html'
    )),
]

# Serve static files in development
if settings.DEBUG:  # Only serve static files in debug mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Optional: serve media files too
