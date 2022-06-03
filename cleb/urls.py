"""cleb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ksg.views import LicView_view, index, CreateLic, LicUpdateView, DeleteLicView
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('ksg/',include('ksg.urls')),
    path('', index, name='home'),
    path('LicView/', LicView_view.as_view(),name='LicView_view'),
    path('LicView/create', CreateLic, name='LicView_create'),
    path('LicView/<int:pk>/update',LicUpdateView.as_view(), name='LicView_update'),
    path('LicView/<int:pk>/delete',DeleteLicView.as_view(), name='LicView_delete'),
    path('app/', include('app.urls')),
    path('sp/', include('sp.urls')),
    path('szp/', include('szp.urls')),
    path('szp1/', include('szp1.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
