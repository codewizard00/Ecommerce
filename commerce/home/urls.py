from . import views
from django.urls import path, include

urlpatterns = [
    path("",views.home,name="home"),
    path("add-to-cart/",views.addtocart , name="addtocart"),
    path("cart/",views.cart , name="cart"),
    path("product/",views.product, name="product"),
    path("product/<int:id>",views.product_details,name="details"),
    path("signup/",views.usersignup , name="signup"),
    path("login/",views.user_login,name="user_login"),
    path("logout/",views.user_logout,name="user_logout"),
    path("pluscart/",views.pluscart,),
    path("checkout",views.checkout,name="checkout")
]
