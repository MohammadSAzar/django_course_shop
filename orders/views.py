from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'سبد خرید شما خالی است، ابتدا محصولی به آن اضافه کنید')
        return redirect('shop')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    number=item['number'],
                    price=product.price,
                )
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            # messages.success(request, 'سفارش شما با موفقیت ثبت شد')
            # order_form = OrderForm()
            request.session['order_id'] = order_obj.id
            return redirect('payment_process')

    context = {
        'form': order_form,
    }
    return render(request, 'orders/order_create.html', context)
