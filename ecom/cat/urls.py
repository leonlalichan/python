from django.urls import path
from . import views
app_name = 'cat'


urlpatterns = [
    path('add/<int:productid>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:productid>/', views.remove, name='remove'),
    path('fullremove/<int:productid>/', views.fullremove, name='fullremove'),
]
