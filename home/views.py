from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import * 
# Create your views here.
def inicio_view(request):
    return render(request,'inicio.html')

def about_view(request):
    return render(request,'about.html')

def contacto_view(request):
    c = ""
    a = ""
    t = ""
    enviado = False
    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            enviado = True
            c = formulario.cleaned_data['correo']
            a = formulario.cleaned_data['titulo']
            t = formulario.cleaned_data['texto']
    else: #GET
              formulario = contacto_form()          

    formulario = contacto_form()

    return render(request,'contacto.html', locals())    

def productos_view(request):

    productos = Producto.objects.filter() #Select * From 'Producto'
    
    return render(request,'productos.html',locals())

def marcas_view(request):

    marcas = Marca.objects.filter()

    return render(request,'marcas.html',locals())  

def categorias_view(request):

    categorias = Categoria.objects.filter()

    return render(request,'categorias.html',locals())      

def agregar_producto_view (request):

    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/')
    else:#GET
        formulario = agregar_producto_form()

    if request.user.is_superuser:
        return render (request, 'agregar_producto.html',locals())
    else:
        return render (request, 'inicio.html',locals()) 

def agregar_marca_view(request):
    if request.method == 'POST':
        formulario = agregar_marca_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/marcas/')
    else:
        formulario = agregar_marca_form()   

    return render (request, 'agregar_marca.html',locals())

def agregar_categoria_view(request):
    if request.method == 'POST':
        formulario = agregar_categoria_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')
    else:
        formulario = agregar_categoria_form()

    return render (request, 'agregar_categoria.html',locals())    
         
def ver_producto_view(request,id_prod):
    
    detalle = Producto.objects.get(id=id_prod) #select * from 'home_producto' where id == id_prod
    #JOINS O SUBCONSULTAS para las categorias del producto
    #tambien se pueden hacer con querysets


    return render(request,'ver_producto.html',locals())                     
            
def eliminar_producto_view(request,id_prod):
    objeto = Producto.objects.get(id=id_prod)
    objeto.delete()
    return redirect('/productos/') 

def editar_producto_view(request,id_prod):
    objeto = Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/')
    else:        
        formulario = agregar_producto_form(instance=objeto)

    return render(request,'agregar_producto.html',locals())   

def ver_marca_view(request,id_marca):
    detalle = Marca.objects.get(id=id_marca)
    return render(request,'ver_marca.html',locals())    

def eliminar_marca_view(request,id_marca):
    objeto = Marca.objects.get(id=id_marca)
    objeto.delete()
    return redirect('/marcas/') 

def editar_marca_view(request,id_marca):
    objeto = Marca.objects.get(id=id_marca)
    if request.method == 'POST':
        formulario = agregar_marca_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/marcas/')
    else:        
        formulario = agregar_marca_form(instance=objeto)

    return render(request,'agregar_marca.html',locals()) 


def ver_categoria_view(request,id_categoria):
    detalle = Categoria.objects.get(id=id_categoria)
    return render(request,'ver_categoria.html',locals())    

def eliminar_categoria_view(request,id_categoria):
    objeto = Categoria.objects.get(id=id_categoria)
    objeto.delete()
    return redirect('/categorias/') 

def editar_categoria_view(request,id_categoria):
    objeto = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        formulario = agregar_categoria_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')
    else:        
        formulario = agregar_marca_form(instance=objeto)

    return render(request,'agregar_marca.html',locals()) 





def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario'] 
            cla = formulario.cleaned_data['clave'] 
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request,usuario)
                return redirect('/')
            else:
                msj = 'usuario o clave incorrectos'  
    else:#GET
        formulario = login_form()
    return render(request,'login.html',locals())    

def logout_view(request):
    logout(request)
    return redirect('/login/')    