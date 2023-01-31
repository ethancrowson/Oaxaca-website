from django.shortcuts import render

# Create your views here.


def index(request):

    dish_data = [
        [1, "Apple Pie", 0, 3.50, 1200, False, "DES"],
        [2, "Bagel", 1, 1.50, 300, True, "BKY"],
        [3, "Baguette", 0, 1.00, 250, False, "BKY"],
        [4, "Naked Beans", 0, 2.00, 500, False, "BFT"],
        [5, "Beef Stew", 234, 4.00, 800, True, "MAIN"],
        [6, "Beef Burger", 0, 3.50, 600, False, "MAIN"],
        [7, "Biscuits", 0, 1.50, 300, False, "DES"],
        [8, "Blueberry Pie", 0, 3.70, 1150, False, "DES"],
        [9, "Carrot Cake", 0, 4.00, 1000, False, "DES"],
        [10, "Casserole", 0, 400.50, 1200, False, "MAIN"],

    ]

    dish_list = []

    for i in range(len(dish_data)):
        dish_list.append({
            "dish_id": dish_data[i][0],
            "dish_name": dish_data[i][1],
            "dish_qty": dish_data[i][2],
            "dish_price": dish_data[i][3],
            "dish_cal": dish_data[i][4],
            "dish_avail": dish_data[i][5],
            "dish_cat": dish_data[i][6],
        })

    return render(request, 'restaurant/index.html', {"dish_list": dish_list})
