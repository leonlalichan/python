from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ecomapp.models import Product
from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, Cartitem

# Create your views here.

def _cartid(request):
    cart = request.session.session_key
    if not cart:
        request.session.save()  # Change to save session
        cart = request.session.session_key  # Get session key after saving

    return cart

def add_cart(request, productid):
    product = Product.objects.get(id=productid)
    try:
        cart = Cart.objects.get(cartid=_cartid(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cartid=_cartid(request))
    try:
        cartitem = Cartitem.objects.get(product=product, cart=cart)
        if  cartitem.quantity < cartitem.product.stock:

            cartitem.quantity += 1
        cartitem.save()
    except Cartitem.DoesNotExist:
        cartitem = Cartitem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
    return redirect('cat:cart_detail')

def cart_detail(request):
    total = 0
    counter = 0
    try:
        cart = Cart.objects.get(cartid=_cartid(request))
        cartitems = Cartitem.objects.filter(cart=cart, active=True)
        for cartitem in cartitems:
            total += (cartitem.product.price * cartitem.quantity)
            counter += cartitem.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'cartitems': cartitems, 'counter': counter, 'total': total})

def remove(request, productid):
    cart = Cart.objects.get(cartid=_cartid(request))
    product = get_object_or_404(Product, id=productid)
    cartitem = Cartitem.objects.get(product=product, cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity -= 1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cat:cart_detail')

def fullremove(request, productid):
    cart = Cart.objects.get(cartid=_cartid(request))
    product = get_object_or_404(Product, id=productid)
    cartitem = Cartitem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('cat:cart_detail')
