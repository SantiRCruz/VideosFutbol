from django.urls import path
from .views import *
urlpatterns = [
    path('',inicio_view, name = 'inicio_view'),
    path('about/',about_view, name ='about_view'),
    path('contacto/',contacto_view, name='contacto_view'),
    path('productos/',productos_view, name='productos_view'),
    path('marcas/',marcas_view, name = 'marcas_view'),
    path('categorias/',categorias_view, name= 'categorias_view'),


    path('agregar_producto/',agregar_producto_view, name = 'agregar_producto'),
    path('agregar_marca/',agregar_marca_view, name = 'agregar_marca'),
    path('agregar_categoria/',agregar_categoria_view, name = 'agregar_categoria'),


    path('ver_producto/<int:id_prod>',ver_producto_view, name = 'ver_producto_view'),
    path('eliminar_producto/<int:id_prod>',eliminar_producto_view, name = 'eliminar_producto_view'),
    path('editar_producto/<int:id_prod>',editar_producto_view, name = 'editar_producto_view'),

    path('ver_marca/<int:id_marca>',ver_marca_view, name = 'ver_marca_view'),
    path('eliminar_marca/<int:id_marca>',eliminar_marca_view, name = 'eliminar_marca_view'),
    path('editar_marca/<int:id_marca>',editar_marca_view, name = 'editar_marca_view'),

    path('ver_categoria/<int:id_categoria>',ver_categoria_view, name = 'ver_categoria_view'),
    path('eliminar_categoria/<int:id_categoria>',eliminar_categoria_view, name = 'eliminar_categoria_view'),
    path('editar_categoria/<int:id_categoria>',editar_categoria_view, name = 'editar_categoria_view'),



    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
]