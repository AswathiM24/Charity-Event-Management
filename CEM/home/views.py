import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
import environ
import razorpay
from django.views.decorators.csrf import csrf_exempt
from user.models import payments

env = environ.Env()
razorpay_client = razorpay.Client(
    auth=(env('RAZOR_KEY_ID'), env('RAZOR_KEY_SECRET')))

currency = 'INR'


def new_order(request):
    amount = int(request.POST['amount']) * 100
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler'

    obj = payments()
    obj.amount = amount /100
    obj.name = request.POST['name']
    obj.phone = request.POST['phone']
    obj.order_id = razorpay_order_id
    obj.merchant_key = env('RAZOR_KEY_ID')
    obj.save()


    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': env('RAZOR_KEY_ID'),
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url,
    }

    return JsonResponse(context)


def homepage(request):
    return render(request, 'home/homepage.html')

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:

            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            result = razorpay_client.utility.verify_payment_signature(
                params_dict)

            if result is not None:
                obj=  payments.objects.get(order_id=razorpay_order_id)
                amount = obj.amount * 100
                try:

                    razorpay_client.payment.capture(payment_id, amount)

                    obj.status =True
                except:
                    pass
        except:
            pass

    return redirect('landing_page')

