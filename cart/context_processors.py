from .cart import Cart

def cp_cart(request):
    return {'cart': Cart(request)}

