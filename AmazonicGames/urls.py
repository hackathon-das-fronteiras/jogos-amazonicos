"""AmazonicGames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from base.views import traducao, is_logged, sair, mylogin, insert_user
from quiz.views import questao, responder, ranking_view

urlpatterns = [
                  path('i18n/', include('django.conf.urls.i18n')),
                  path('admin/', admin.site.urls),
                  url(r'^$', TemplateView.as_view(template_name='home.html')),
                  url(r'^traducao/$', traducao, name="traducao"),
                  url(r'^is_logged/$', is_logged, name="is_logged"),
                  url(r"^logout/$", sair, name="logout"),
                  url(r"^mylogin/$", mylogin, name="mylogin"),
                  url(r"^insertuser/$", insert_user, name="insert_user"),
                  url(r"^questao/$", questao, name="questao"),
                  url(r"^responder/$", responder, name="responder"),
                  url(r"^ranking/$", ranking_view, name="ranking"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static('/webfonts', document_root=settings.WEBFONTS_ROOT)