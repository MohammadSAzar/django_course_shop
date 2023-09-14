from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس خود را وارد کنید...'}),
            'notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'توضیحات خود را وارد کنید...'}),
        }

