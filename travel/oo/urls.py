from.import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),

]