from django.urls import path, include
from szp1 import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('SZP1create', views.SZP1create, name='SZP1create'),
    path('', views.SZP1Lic_view.as_view(), name='SZP1_view'),
    path('<int:pk>/update', views.SZP1LicUpdateView.as_view(), name='SZP1_update'),
    path('<int:pk>/delete', views.SZP1DeleteLicView.as_view(), name='SZP1_delete'),
    path('snippet', views.SnippetListView.as_view(),name='szp1_list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)