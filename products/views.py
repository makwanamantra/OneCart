from django.shortcuts import render,get_object_or_404
from .models import Product

def products(request):
    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })
def detail(request,product_id):
    o=get_object_or_404(Product,pk=product_id)
    return render(request,'ParticularProduct.html',{'product':o})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product, Cart, CartItem
@login_required(login_url='login')
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')
@login_required(login_url='login')
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity < item.product.stock:
        item.quantity += 1
        item.save()

    return redirect('cart')
@login_required(login_url='login')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()

    return redirect('cart')
@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get or create user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if product already exists in cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        # Product already exists, increase quantity
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Quantity updated.")
        else:
            messages.error(request, "Product is out of stock.")
    else:
        messages.success(request, "Product added to cart.")

    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = CartItem.objects.filter(cart=cart)

    total = sum(item.product.discounted_price() * item.quantity for item in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total,
    })
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')