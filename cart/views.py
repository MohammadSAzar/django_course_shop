from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .cart import Cart
from .forms import AddToCart
from products.models import Product

def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_number_form'] = AddToCart(initial={
            'number': item['number'],
            'inplace': True,
        })
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)

def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCart(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        number = cleaned_data['number']
        cart.add(product, number, replace_current_number=cleaned_data['inplace'])
    return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_clear(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, 'سبد با موفقیت خالی شد')
    else:
        messages.warning(request, 'سبد شما خالی است')
    return redirect('shop')
