from xml.dom.minidom import Document
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import AtencionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('atencion',AtencionViewset)

urlpatterns = [
    path ('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('indexatencion',views.indexatencion,name='indexatencion'),
    path('crearatencion',views.crearatencion,name='crearatencion'),
    path('editaratencion/<int:id>',views.editaratencion,name='editaratencion'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('contacto',views.contacto,name='contacto'),
    path('api/',include(router.urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

