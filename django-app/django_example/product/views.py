from django.shortcuts import render
from .product import ProductForm
from django.http import JsonResponse
from .models import Product
from .models import Customer
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