from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse


DISHES = {
    1: {"name": "Pizza", "price": 100, "veg": True, "tag": ["italian", "fastfood"], "about": "Pizza is a popular Italian dish made with a round, flat base of dough topped with tomato sauce, cheese, and various toppings such as vegetables, meats, and herbs. It is baked in an oven until the crust is crispy and the cheese is melted and bubbly. Pizza is often served in slices and can be enjoyed as a quick snack or a full meal."},
    2: {"name": "Burger", "price": 60, "veg": False, "tag": ["american", "fastfood"], "about": "A burger is a popular American sandwich consisting of a cooked patty of ground meat, usually beef, placed inside a sliced bun. It is often served with various toppings such as lettuce, tomato, onion, and condiments."},
    3: {"name": "Pasta", "price": 75, "veg": True, "tag": ["italian"], "about": "Pasta is a staple food of traditional Italian cuisine. It is made from durum wheat semolina and water, formed into various shapes and then cooked in boiling water or broth."},
    4: {"name": "Salad", "price": 50, "veg": True, "tag": ["healthy"], "about": "A salad is a dish consisting of a mixture of small pieces of food, typically vegetables. It can be served as a separate dish or as part of a larger meal."},
    5: {"name": "Sushi", "price": 120, "veg": False, "tag": ["japanese"], "about": "Sushi is a traditional Japanese dish made with vinegared rice, seafood, and vegetables. It is often served with soy sauce, wasabi, and pickled ginger."},
    6: {"name": "Tacos", "price": 80, "veg": False, "tag": ["mexican"], "about": "Tacos are a traditional Mexican dish consisting of a folded or rolled tortilla filled with various ingredients such as meat, cheese, beans, and vegetables."}
}
HOURS = {
    "Monday": "9:00 AM - 9:00 PM",
    "Tuesday": "9:00 AM - 9:00 PM",
    "Wednesday": "9:00 AM - 9:00 PM",
    "Thursday": "9:00 AM - 9:00 PM",
    "Friday": "9:00 AM - 9:00 PM",
    "Saturday": "10:00 AM - 8:00 PM",
    "Sunday": "Closed"
}


def home(request):
    menu_items= reverse("menu")
    return HttpResponse(f"welcome to the onepiece cafe! <a href='{menu_items}'>Menu</a>")


def dish(request, dish_id):
    dish = DISHES.get(dish_id)
    if dish_id  not in DISHES:
        raise Http404("we dont have the dish you are looking for")
    name = DISHES[dish_id]["name"]
    price = DISHES[dish_id]["price"]
    return HttpResponse(f"{name} costs  is {price}")

 
def hello(request):
    name = request.GET.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}! you sent a {request.method} request to {request.path}")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")


def menu_page(request):
    dishes=[ {"id":number,**dish} for number,dish in DISHES.items()]
    return render(request,"order/menu.html",{"dishes":dishes})

def about(request):
    return HttpResponse("This is a cafe where you can order your favorite dishes online.there is lots of variety of dishes available here. We are open from 9:00am to 9:00pm. Enjoy your meal!")

def service(request):
    return HttpResponse("We provide home delivery service for your convenience. You can place your order online and we will deliver it to your doorstep. Enjoy our delicious dishes from the comfort of your home!")


def bill(request, dish_id, qty):
    if dish_id not in DISHES:
        raise Http404("Dish not found")
    dish = DISHES[dish_id]
    total = qty * dish["price"]
    return HttpResponse(
        f"<h1>Bill</h1><p>{dish['name']}: {qty} x Rs {dish['price']} = Rs {total}</p>"
        "<p>Thank you for ordering from our cafe!</p>"
    )


def shout(request,word):
    return HttpResponse(f"<h1>Shout</h1><p>{word}!</p>")
 
 
