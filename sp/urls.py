from django.urls import path, include
from sp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('SPcreate', views.SPcreate, name='SPcreate'),
    path('', views.SpLic_view.as_view(), name='SP_view'),
    path('<int:pk>/update', views.SpLicUpdateView.as_view(), name='SP_update'),
    path('<int:pk>/delete', views.SpLicDeleteLicView.as_view(), name='SP_delete'),
    path('snippet', views.SnippetListView.as_view(),name='sp_list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)