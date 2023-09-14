from django import forms

class AddToCart(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, 31)]
    number = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
