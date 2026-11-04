from django.urls import path
from.import views

urlpatterns = [
    path("",views.home),
    path("dish/<int:dish_id>/",views.dish),
    path("hello/",views.hello),
    path("menu/",views.menu_page),
]