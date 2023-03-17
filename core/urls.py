from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('blog/',views.blog,name='blog'),
    path('checkout/',views.checkout,name='checkout'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('login/',views.login,name='login'),
    path('tracking/',views.tracking,name='tracking'),
    path('register/',views.signup,name='signup'),
    path('single_blog/',views.single_blog,name='single_blog')
    
    
]