from django.urls import path, include
from . import views


urlpatterns = [
    path('place_order/',views.place_order,name='place_order'),
    path('payments/',views.payments,name='payments'),

    path('razorpay/', views.razorpay, name='razorpay'),
    path('payments_completed/',views.payments_completed,name = 'payments_completed'),
]