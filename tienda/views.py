from django.shortcuts import render , get_object_or_404

from .models import * 
# Create your views here.
def index(request):
    category_list = Categoria.objects.all()
    product_list = Producto.objects.order_by('nombre')[:6]
    context ={'product_list':product_list , 'category_list':category_list}
    return render(request,'index.html' , context)

def producto(request , producto_id):
    category_list = Categoria.objects.all()
    producto = get_object_or_404(Producto , pk=producto_id)
    return render(request,'producto.html',{'producto':producto, 'category_list':category_list})

def categoria(request , categoria_id):
    category_list = Categoria.objects.all()
    productos = Producto.objects.filter(categoria = categoria_id)
    return render(request , 'listar.html' , {'productos': productos ,'category_list':category_list})

