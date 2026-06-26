from django.urls import path
from . import views as v

urlpatterns = [

    # Product list
    path('', v.products, name='products'),

    # Product detail
    path('<int:product_id>/', v.detail, name='product_detail'),
    path('cart/', v.cart, name='cart'),
    # Cart actions
    path('cart/add/<int:product_id>/', v.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', v.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', v.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', v.remove_from_cart, name='remove_from_cart'),
]