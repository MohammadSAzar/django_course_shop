from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Product, Review
from .forms import ReviewForm
from cart.forms import AddToCart

class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    paginate_by = 6
    context_object_name = 'products'
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ReviewForm()
        context['add_to_cart_form'] = AddToCart()
        return context


class CommentCreateView(CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        return super().form_valid(form)

# def product_detail_view(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     comments = product.comments.filter(active=True)
#     if request.method == 'POST':
#         comment_form = ReviewForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.product = product
#             new_comment.author = request.user
#             new_comment.save()
#             comment_form = ReviewForm()
#     else:
#         comment_form = ReviewForm()
#     context = {
#         'product': product,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#     return render(request, 'products/product_detail.html', context)


