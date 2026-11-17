from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
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
    return render(request, "order/home.html")


def dish(request, dish_id):
    selected_dish = DISHES.get(dish_id)
    if selected_dish is None:
        raise Http404("we dont have the dish you are looking for")
    return render(request, "order/dish.html", {"dish": selected_dish})

 
def hello(request):
    name = request.GET.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}! you sent a {request.method} request to {request.path}")


def hello_name(request, name):
    return render(request, "order/name.html", {"name": name})



def menu_page(request):
    dishes=[ {"id":number,**dish} for number,dish in DISHES.items()]
    return render(request,"order/menu.html",{"dishes":dishes})

def about(request):
    return render(request, "order/about.html")

def service(request):
    return render(request, "order/service.html")


def bill(request, dish_id, qty):
    if dish_id not in DISHES:
        raise Http404("Dish not found")
    dish = DISHES[dish_id]
    total = qty * dish["price"]
    return render(request, "order/bill.html", {
        "dish": dish,
        "qty": qty,
        "total": total
    })


def shout(request,word):
    return HttpResponse(f"<h1>Shout</h1><p>{word}!</p>")
 

def order_page(request):
    if request.method == "POST":
        dish_id = int(request.POST.get("dish_id", 0))
        qty = int(request.POST.get("qty", 0))

        if dish_id not in DISHES:
            raise Http404("Dish not found")

        return redirect("bill", dish_id=dish_id, qty=qty)
    return render(request, "order/place_order.html")