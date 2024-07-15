"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.travel.urls")),
    path('mypage/', login_required(TemplateView.as_view(template_name='mypage.html')), name='mypage'),
    path('accounts/', include('allauth.urls')),
    path('  /', login_required(TemplateView.as_view(template_name='profile.html')), name='profile'),
    path('baenangtalk/', include("apps.baenangtalk.urls")),
    path('flights/',include('apps.flights.urls',namespace='flights')),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
