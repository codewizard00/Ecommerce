from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q

from django.contrib.auth import authenticate, login , logout
# Create your views here.
def home(request):
    return render(request , "index.html")

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shiping_amount=70.0
        total_amount = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user==user]
        if cart_products:
            for p in cart_products:
                tempamount = (p.quantity*p.product.product_price)
                amount += tempamount
                totalamount=amount+shiping_amount

        return render(request,"cart.html",{"carts":cart,"totalamount":totalamount,"amount":amount})
    else:
        return render(request,"signup.html")
        


def addtocart(request):
    user=request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def product(request):
    products = Product.objects.all()
    return render(request,'products.html',{"products":products})

def product_details(request,id):
    product = Product.objects.get(pk=id)
    return render(request, "products-details.html",{"product":product})
    
def usersignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_obj = User.objects.create_user(username=username,email=email,password=password)
        user_obj.save()
        return render(request,"login.html")
    else:
        return render(request,"login.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            
        else:
            return render(request,"login.html")

def pluscart(request):
    if request.method=="GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        amount = 0.0
        shiping_amount = 70.0
        total_amount = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_products:
            for p in cart_products:
                tempamount = (p.quantity*p.product.product_price)
                amount += tempamount
                totalamount=amount+shiping_amount

            data={
                "quantity" : c.quantity,
                "amount" : amount,
                "tempamount" : tempamount
            }

            return JsonResponse(data)

def checkout(request):
    return render(request ,"checkout.html")


def user_logout(request):
    logout(request)
    return redirect("/")