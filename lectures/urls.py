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

from .views import (lectures_create,
                    lectures_retrieve,
                    lectures_list,
                    lectures_update,
                    lectures_delete)

urlpatterns = [
    url(r'^create/$', lectures_create),
    url(r'^retrieve/$', lectures_retrieve),
    url(r'^list/$', lectures_list),
    url(r'^update/$', lectures_update),
    url(r'^delete/$', lectures_delete),
]
