from .models import Cart, Cartitem
from .views import _cartid

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {'item_count': 0}  # Return 0 item count for admin paths
    else:
        try:
            cart = Cart.objects.get(cartid=_cartid(request))
            cartitems = Cartitem.objects.filter(cart=cart)
            for cartitem in cartitems:
                item_count += cartitem.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return {'item_count': item_count}

