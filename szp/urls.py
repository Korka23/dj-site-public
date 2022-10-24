from django.urls import path, include
from szp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('SZPcreate', views.SZPcreate, name='SZPcreate'),
    path('', views.SZPLic_view.as_view(), name='SZP_view'),
    path('<int:pk>/update', views.SZPLicUpdateView.as_view(), name='SZP_update'),
    path('<int:pk>/delete', views.SZPDeleteLicView.as_view(), name='SZP_delete'),
    path('snippet', views.SnippetListView.as_view(),name='szp_list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)