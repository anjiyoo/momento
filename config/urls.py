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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.userinfo.views import profile  # profile 뷰를 임포트합니다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.travel.urls")),
    path('mypage/', profile, name='mypage'),
    path('accounts/', include('allauth.urls')),
    # 필요없는 url들은 홈으로 리디렉션 처리
    # 특정 URL 패턴들을 홈으로 리디렉션
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
