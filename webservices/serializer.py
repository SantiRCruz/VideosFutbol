from rest_framework import serializers
from home.models import *

class Producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Producto
        fields = ('url','nombre','descripcion','precio','cantidad','activo','foto','marca','categorias',) 

class Marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Marca
        fields = ('url','nombre',) 

class Categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Categoria
        fields = ('url','nombre',)                 