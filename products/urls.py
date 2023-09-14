from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='shop'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
    re_path(r'(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product_detail'),
]




