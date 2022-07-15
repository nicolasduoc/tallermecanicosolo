from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Atencion
from .forms import AtencionForm, ContactoForm
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenido amigos</h1>")

def index(request):
    return render(request,'index.html')

def indexatencion(request):
    Atenciones = Atencion.objects.all()
    return render(request,'indexatencion.html',{'Atenciones': Atenciones})

def crearatencion(request):
    formulario = AtencionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('indexatencion')
    return render(request,'crearatencion.html',{'formulario': formulario})

def editaratencion(request,id):
    atencion = Atencion.objects.get(id=id)
    formulario = AtencionForm(request.POST or None, request.FILES or None, instance=atencion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect(indexatencion) 
    return render(request,'editaratencion.html',{'formulario':formulario})

def nosotros(request):
    return render(request,'nosotros.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado"
        else:
            data["form"] = formulario

    return render(request,'contacto.html',data)

def eliminar(request,id):
    atencion = Atencion.objects.get(id=id)
    atencion.delete()
    return redirect('indexatencion')