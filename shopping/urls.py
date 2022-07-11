
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index , name="Home"),
    path("basic", views.basic , name="basic"),
    path("about", views.about , name="about"),
    path("contact", views.contact , name="contact"),
    path("tracker", views.tracker , name="tracker"),
    path("checkout", views.checkout , name="checkout"),
    path("productsview/<int:myid>", views.productsview, name="productsview"),
    path("search", views.search , name="search"),
    path("razorpayy", views.razorpayy , name="razorpayy"),
 
]