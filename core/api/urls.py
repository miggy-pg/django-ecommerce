from django.urls import path

from .views import ItemListView
from .views import AddToCartView

urlpatterns = [
    path('product-list/', ItemListView.as_view(), name='product_list'),
    path('add-to-cart/', ItemListView.as_view(), name='add_to_cart')
]