from django import forms

DISHES = { 
    1: {"name": "Pizza", "price": 100, "veg": True, "tag": ["italian", "fastfood"], "about": "Pizza is a popular Italian dish made with a round, flat base of dough topped with tomato sauce, cheese, and various toppings such as vegetables, meats, and herbs. It is baked in an oven until the crust is crispy and the cheese is melted and bubbly. Pizza is often served in slices and can be enjoyed as a quick snack or a full meal."},
    2: {"name": "Burger", "price": 60, "veg": False, "tag": ["american", "fastfood"], "about": "A burger is a popular American sandwich consisting of a cooked patty of ground meat, usually beef, placed inside a sliced bun. It is often served with various toppings such as lettuce, tomato, onion, and condiments."},
    3: {"name": "Pasta", "price": 75, "veg": True, "tag": ["italian"], "about": "Pasta is a staple food of traditional Italian cuisine. It is made from durum wheat semolina and water, formed into various shapes and then cooked in boiling water or broth."},
    4: {"name": "Salad", "price": 50, "veg": True, "tag": ["healthy"], "about": "A salad is a dish consisting of a mixture of small pieces of food, typically vegetables. It can be served as a separate dish or as part of a larger meal."},
    5: {"name": "Sushi", "price": 120, "veg": False, "tag": ["japanese"], "about": "Sushi is a traditional Japanese dish made with vinegared rice, seafood, and vegetables. It is often served with soy sauce, wasabi, and pickled ginger."},
    6: {"name": "Tacos", "price": 80, "veg": False, "tag": ["mexican"], "about": "Tacos are a traditional Mexican dish consisting of a folded or rolled tortilla filled with various ingredients such as meat, cheese, beans, and vegetables."}
}

DISH_Choices = [(dish_id, f"{info['name']} - Rs {info['price']}") for dish_id, info in DISHES.items()]


class OrderForm(forms.Form):
    customer_name = forms.CharField(
        max_length=100, 
        label="Your Name", 
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    
    dish_id = forms.TypedChoiceField(
        choices=DISH_Choices, 
        coerce=int, 
        label="Select Dish"
    )

    quality = forms.IntegerField(
        min_value=1, 
        label="Quantity", 
        widget=forms.NumberInput(attrs={"placeholder": "Enter quantity"})
    )
    
    parcel = forms.BooleanField(
        required=False, 
        label="Parcel order", 
        initial=False
    )
