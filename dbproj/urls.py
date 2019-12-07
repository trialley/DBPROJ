"""dbproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.documentation import include_docs_urls

# xadmin自动寻找可以管理的数据表
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # path('', xadmin.site.urls),
    path("", RedirectView.as_view(url='/api/houses/docs/')),

    path('xadmin/', xadmin.site.urls),
    path('api/houses/docs/', include_docs_urls(title='文档')),



    path('api/houses/', include('houses.api.urls', namespace='houses')),
    # 每当 Django 遇到 include() 时，
    # 它会截断与此项匹配的 URL 的部分，
    # 并将剩余的字符串发送到 URLconf 以供进一步处理。
    # path('houses/', include('houses.urls')),
    path('admin/', admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url='static/favicon.ico')),
]
