"""
URL configuration for academy project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.i18n import set_language

admin.site.site_header = 'پنل ادمین البرز'
admin.site.index_title = 'ادمین بخش آموزش'

urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path('v1/api/', include('default.urls')),
    path('v1/core/', include('core.urls')),
    path('v1/forms/', include('forms.urls')),
    path('set_language/', set_language, name='set_language'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
