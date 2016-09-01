"""CHCWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^lectures/', include('lectures.urls')),
    url(r'^writeups/', include('writeups.urls')),
    url(r'^guides/', include('guides.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^sponsorship$', TemplateView.as_view(template_name='sponsorship.html'), name="sponsorship"),
    url(r'^faq$', TemplateView.as_view(template_name='faq.html'), name="faq"),
    url(r'^tools$', TemplateView.as_view(template_name='tools.html'), name="tools"),
]

admin.site.site_header = 'Cornell Hacking Club Admin Page'

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)