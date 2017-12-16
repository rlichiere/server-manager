"""servermanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin

import views
import forms


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('applications.urls')),

    url(r'^readme$', views.ReadmeView.as_view(), name='readme'),
    url(r'^login/$', auth_views.login, {'template_name': 'front/login.html',
                                        'authentication_form': forms.FrontAuthForm}, name='front-login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='front-logout'),
]
