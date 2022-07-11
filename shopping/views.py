from django.shortcuts import render
from .models import *
from math import ceil
import razorpay


# Create your views here.
def index(request):

    #params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    #allproducts = [[products,range(1,len(products)),nSlides],[products,range(1,len(products)),nSlides]]

    allproducts = []
    category_products = Product.objects.values('category', 'id')
    cats = {item["category"] for item in category_products}

    for m in cats:
        prod = Product.objects.filter(category=m)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        # 27//4 + ceil(27/4 - 27//4) = 6+ ceil(6.75 - 6)= 6+ ceil(0.75)= 6+1=7
       # 24//4 + ceil(24/4 -24//4) = 6 + ceil(6-6)= 6+ceil(0)= 6
        allproducts.append([prod, range(1, nSlides), nSlides])

    params = {'allproducts': allproducts}
    return render(request, 'shopping/index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allproducts = []
    category_products = Product.objects.values('category', 'id')
    cats = {item["category"] for item in category_products}
    for m in cats:
        prodtemp = Product.objects.filter(category=m)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            allproducts.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allproducts, "msg": ""}
    if len(allproducts) == 0 or len(query) < 4:
        params = {
            'msg': "No such product found , try to enter another product (Minimum 4 letters required)"}
    return render(request, 'shopping/search.html', params)


def basic(request):
    return render(request, 'shopping/basic.html')


def about(request):
    return render(request, 'shopping/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", '')
        email = request.POST.get("email", '')
        phone_no = request.POST.get("phone", '')
        comment = request.POST.get("comment", '')
        contact = Contact(name=name, email=email,
                          phone_no=phone_no, comment=comment)
        contact.save()

    return render(request, 'shopping/contact.html')


def tracker(request):
    return render(request, 'shopping/tracker.html')


def productsview(request, myid):
    # here we are going to list products
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shopping/productsview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        firstname = request.POST.get("firstname", '')
        lastname = request.POST.get("lastname", '')
        email = request.POST.get("email", '')
        address = request.POST.get("address", '')
        address2 = request.POST.get("address2", '')
        Country = request.POST.get("Country", '')
        State = request.POST.get("State", '')
        zip_code = request.POST.get("zip_code", '')
        phone = request.POST.get("phone", '')

        order = Orders(items_json=items_json, firstname=firstname, lastname=lastname, email=email,
                       address=address, address2=address2, phone=phone, Country=Country, State=State, zip_code=zip_code,)
        order.save()
        thank = True
        id = order.Order_id
        return render(request, 'shopping/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shopping/checkout.html')


def razorpayy(request):
    client = razorpay.Client(
        auth=("rzp_test_NHphcLQwPltWO4", "hJQcKcye31mAJ2TrZ57Ko8vw"))

    order_amount = 50000
    order_currency = 'INR'

    client.order.create(
        dict(amount=order_amount, currency=order_currency, payment_capture=1))

    # saved address
    #final_address = Orders.objects.all()
    #id = final_address.Order_id
    return render(request, 'shopping/razorpayy.html')
