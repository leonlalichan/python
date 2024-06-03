from django.urls import path, include

from .import views
app_name='ecomapp'
urlpatterns = [

    path('',views.allProductCat,name='allProductCat'),
    path('<slug:cslug>/',views.allProductCat,name='productsby'),
    path('<slug:cslug>/<slug:productslug>/',views.proDetail,name='prodCatDetail')

]