from django.http import HttpResponse,Http404


DISHES = {
    1: ("Pizza", 90),
    2: ("Burger", 60),
    3: ("Pasta", 75),
    4: ("Salad", 50)
}

def home(request):
    return HttpResponse("Welcome to the Cafe!")


def dish(request, dish_id):
    dish = DISHES.get(dish_id)
    if dish_id  not in DISHES:
        raise Http404("we dont have the dish you are looking for")
    name, price = DISHES[dish_id]
    return HttpResponse(f"{name} costs  is {price}")

 
def hello(request):
    name = request.GET.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}! you sent a {request.method} request to {request.path}")


def menu_page(request):
    items = " "
    for number, (name, price) in DISHES.items():
        items += f"<li>{number}.{name } - Rs{price}</li>"
    return HttpResponse(f"<h1>Cafe Menu</h1><ul>{items}</ul>")