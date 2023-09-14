from products.models import Product

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, number=1, replace_current_number=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'number': 0}
        if replace_current_number:
            self.cart[product_id]['number'] = number
        else:
            self.cart[product_id]['number'] += number
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            item['total_price'] = item['number'] * item['product_obj'].price
            yield item

    def __len__(self):
        return sum(item['number'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def total_price(self):
        # product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids)
        return sum(item['number'] * item['product_obj'].price for item in self.cart.values())

    def is_empty(self):
        if self.cart:
            return False
        return True



