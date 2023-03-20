from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('checkout/',views.checkout,name='checkout'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('tracking/',views.tracking,name='tracking'),
    path('single_blog/',views.single_blog,name='single_blog')
    
    
]