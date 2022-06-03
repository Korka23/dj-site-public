from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('Appcreate', views.Appcreate, name='Appcreate'),
    path('', views.LicAppNew_view.as_view(), name='App_view'),
    path('<int:pk>/update', views.AppLicUpdateView.as_view(), name='App_update'),
    path('<int:pk>/delete', views.AppDeleteLicView.as_view(), name='App_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)