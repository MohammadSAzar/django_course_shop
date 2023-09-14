from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    first_name = models.CharField(max_length=150, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=15, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=1000, verbose_name=_('Address'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is_Paid?'))
    notes = models.CharField(max_length=1000, verbose_name=_('Notes'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('date $ time of creation'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('date $ time of modification'))

    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    number = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Order Item {self.id}: {self.product}x{self.number}'


