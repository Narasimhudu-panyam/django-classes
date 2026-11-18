from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("hello/", views.hello, name="hello"),
    path("our_menu/", views.menu_page, name="menu"),
    path("dish/<int:dish_id>/", views.dish, name="dish"),
    path("hello/<str:name>/", views.hello_name, name="hello_name"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("bill/<int:dish_id>/<int:qty>/", views.bill, name="bill"),
    path("shout/<str:word>/", views.shout, name="shout"),
    path("place_order/", views.order_page, name="place_order"),
    path("order/", views.order_page, name="order"),
]
