from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path ('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('indexatencion',views.indexatencion,name='indexatencion'),
    path('crearatencion',views.crearatencion,name='crearatencion'),
    path('editaratencion/<int:id>',views.editaratencion,name='editaratencion'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('contacto',views.contacto,name='contacto')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

