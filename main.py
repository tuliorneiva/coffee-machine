MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def count_money():
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    money = quarters + dimes + nickles + pennies
    return money


def check_ingredients(ask_order):
    for key in MENU[ask_order]["ingredients"]:
        ingredient, quantity = key, MENU[ask_order]["ingredients"][key]
        resources[ingredient] -= quantity
    return resources


def check_money(ask_order, money, profit):
    price = MENU[ask_order]['cost']
    if money >= price:
        change = money - price
        print(f"Here is ${change} in change")
        profit += price
    else:
        print("Sorry, that's not enough money. Money refunded.")
    return profit


turn_off = False
while turn_off == False:
    ask_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ask_order == 'off':
        turn_off = True
    elif ask_order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif ask_order == 'profit':
        print(f"Total profit: ${profit}")
    else:
        resources = check_ingredients(ask_order)
        positive_resources = True
        for key in resources:
            if resources[key] < 0:
                print(f"Sorry, there's not enough {key}")
                positive_resources = False
                break
        if positive_resources == True:
            money = count_money()
            profit = check_money(ask_order, money, profit)
            print(f"Here is your {ask_order}. Enjoy!")