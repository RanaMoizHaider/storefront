from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import HttpResponse
from django.db.models import Q, F
from django.db import transaction, connection
from store.models import Product, Collection, Order, OrderItem

# @transaction.atomic()

def say_hello(request):
    # return HttpResponse('Hello World')

    # products = Product.objects.all()
    #
    # for product in products:
    #     print(product)

    # product = Product.objects.get(pk=1)

    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # None
    # product = Product.objects.filter(pk=0).first()

    # Bool
    # exists = Product.objects.filter(pkk=0).exists()

    # products = Product.objects.filter(unit_price__range=(20, 30))

    # products = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # products = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # products = Product.objects.filter(inventory=F('unit_price'))

    # Creating new object
    # collection = Collection()
    # collection.title = 'Game'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    # Updating object using this will update all the attributes even those are not mentioned
    # collection = Collection(pk=11)
    # collection.title = 'Game'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    # Best update method
    # Collection.objects.filter(pk=11).update(featured_product=None)

    # Collection.objects.filter(pk=12).delete()

    # This statement will run both queries if there is an error in any one query
    # then both of them will be cancelled and not any one of them will be excecuted.
    # ...
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    # Adding raw queries
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM store_collection')

    # Calling store procedure
    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [0,1,'a'])

    # Raw queries without with block must be closed
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM store_collection')
    # cursor.close()

    return render(request, 'hello.html', {'name': 'Moiz'})