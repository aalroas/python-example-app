from django.shortcuts import render
from .product import ProductForm
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Product
from .models import Customer
from django.core import serializers
from django.db.models import F

# Create your views here.

def product_view(request):
    product = ProductForm()
    
    response_data = {}

    if request.POST.get('action') == 'post':
        
        customer_id = request.POST.get('customer_id')
        customer_name = request.POST.get('customer_name')
         
        check = Customer.objects.filter(id=customer_id).exists()
        
        if check != 1:  
           customer = Customer.objects.create(
            id = customer_id,
            name = customer_name,
            ) 

        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')

        response_data['name'] = name
        response_data['price'] = price
        response_data['description'] = description
    

        product = Product.objects.create(
            customer_id = Customer.objects.get(pk=customer_id).id,
            name = name,
            price = price,
            description = description,
            )
        product.save() 
        
        return JsonResponse(response_data)
    
    context = {'product': product}
    
    return render(request, 'product/product.html', context)




def product_list(request):
    if request.is_ajax():
        products = Product.objects.select_related('customer').all()

        # new_products = {}
        # for p in products:
        #     new_products['customer_name'] = p.customer
        #     new_products['id'] = p.pk
        #     new_products['name'] = p.name
        #     new_products['price'] = float(p.price)
        #     new_products['description'] = p.description
            
        products_serialized = serializers.serialize('json', products)
        # return JsonResponse(products_serialized, safe=False)
        return HttpResponse(products_serialized, content_type="application/json")
    return render(request, 'product/list.html')


def product_find(request):
    if request.is_ajax():  
        customer_id = request.POST.get('customer_id')
        products = Product.objects.filter(customer=customer_id)
        products_serialized = serializers.serialize('json', products)
        return HttpResponse(products_serialized, content_type="application/json")
    return render(request, 'product/find.html')

