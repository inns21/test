from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Order
# Create your views here.
def index(request):

    return render(request, 'order/index.html')

def add_order(request):

    if request.method == 'GET':  # 요청 방식이 GET이면 화면 표시
        return render(request, 'order/order_form.html')

    else:
        order_text = request.POST['order_text']
        price = request.POST['price']
        address = request.POST['address']

        Order.objects.create(
            order_text = order_text,
            price = price,
            address = address
        )
        return HttpResponseRedirect('/order/')


def order_list(request):

    order_list = Order.objects.all().order_by('-id')

    context = {
        'order_list': order_list
    }
    return render(request, 'order/order_list.html', context)


def update_order(request, id):
    print(id)
    order = Order.objects.get(id = id)

    if request.method == 'GET':
        context = {'order': order }
        return render(request, 'order/update_order.html', context)
    else:
        order.order_text = request.POST['order_text']
        order.price = request.POST['price']
        order.address = request.POST['address']
        order.save()

    return HttpResponseRedirect('/order/order_list/')


def delete_order(request, id):
    print(id)
    Order.objects.get(id = id).delete()

    return HttpResponseRedirect('/order/order_list/')