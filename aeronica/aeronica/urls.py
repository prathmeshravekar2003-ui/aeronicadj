"""
URL configuration for aeronica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
import os


def serve_text_file(filename, content_type):
    """Return a simple view that serves a static text file from the project root."""
    from django.http import HttpResponse

    def view(request):
        filepath = os.path.join(settings.BASE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type=content_type)
    return view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', serve_text_file('robots.txt', 'text/plain')),
    path('sitemap.xml', serve_text_file('sitemap.xml', 'application/xml')),
    path('', include('main.urls', namespace='main')),
]

# Custom 404 handler
handler404 = 'main.views.handler404'
