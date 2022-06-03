from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.KSGView.as_view(), name='ksg'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDataView.as_view(), name='ksg_detail'),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name='ksg_update'),
    path('<int:pk>/delete', views.DeleteKSG.as_view(), name='ksg_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)