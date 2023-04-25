import razorpay

from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
from django.contrib import messages, auth
from .models import Order
from accounts.models import Account
from store.models import Product, Banner
import datetime
import json
from django.http import JsonResponse
from .models import Order, Payment, OrderProduct
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
from django.views import View


# Create your views here.
# def coupon(request):
#   if request.method == 'POST':
#     coupon_code = request.POST['coupon']
#     grand_total = request.POST['grand_total']
#     coupon_discount = 0
#     try:
#       instance = UserCoupon.objects.get(user = request.user ,coupon__code = coupon_code)

#       if float(grand_total) >= float(instance.coupon.min_value):
#         coupon_discount = ((float(grand_total) * float(instance.coupon.discount))/100)
#         grand_total = float(grand_total) - coupon_discount
#         grand_total = format(grand_total, '.2f')
#         coupon_discount = format(coupon_discount, '.2f')
#         msg = 'Coupon Applied successfully'
#         instance.used = True
#         instance.save()
#       else:
#           msg='This coupon is only applicable for orders more than ₹'+ str(instance.coupon.min_value)+ '\- only!'
#     except:
#             msg = 'Coupon is not valid'
#     response = {
#                'grand_total': grand_total,
#                'msg':msg,
#                'coupon_discount':coupon_discount,
#                'coupon_code':coupon_code,
#                 }

#   return JsonResponse(response)

def payments(request):
    return render(request,'payments.html')
# def razorpay(request):
#     # Initialize Razorpay client with your API key and secret key

#     client = razorpay.Client(auth=("rzp_test_MPWpuoN6V0IZuk", "iSObOXmeFlFgVSBFrX54bCja"))

#     data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
#     payment = client.order.create(data=data)


def payments_completed(request):
    order_number = request.GET.get('order_number')
    transID = request.GET.get('payment_id')
    try:
        order = Order.objects.get(order_number = order_number)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.product.offer_price() * i.quantity

        payment = Payment.objects.get(payment_id=transID)

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal,
        }
        return render(request, 'orders/payment_success.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')

def place_order(request, total=0, quantity=0,):
    current_user = request.user
    
    # if the cart count is less than or equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    
    if cart_count <= 0:
        return redirect('category')
    
    grand_total = 0
    
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing information inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            
            # generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('payments')
        else:
            return redirect('checkout')
    else:
        return redirect('checkout')
        
        
        
def razorpay(request):
    pass