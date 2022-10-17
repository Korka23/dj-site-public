from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('Appcreate', views.Appcreate, name='Appcreate'),
    #path('Appcreate', views.Appcreate_list, name='Appcreate'),
   #path('test', lambda request: render(request, 'test_view.html')),
    path('', views.LicAppNew_view.as_view(), name='App_view'),
     path('<int:pk>/update', views.AppLicUpdateView.as_view(), name='App_update'),
    #path('<int:pk>/update', views.AppLicUpdateView_list, name='App_update'),
    path('<int:pk>/delete', views.AppDeleteLicView.as_view(), name='App_delete'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
    path('ACT', views.AppCreateTest.as_view(), name='ACT'),
    path('tlist', TemplateView.as_view(template_name='app/index.php')),
    path('indus', views.indus),
    path('bbl', views.BootstrapFilterView),
    path('snippet', views.SnippetListView.as_view(),name='app_list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)