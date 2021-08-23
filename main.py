import sys
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.20,
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


# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
def animatron():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def sufficient_resources(order_ingredients):
    """True if order can be made, False if insufficient ingredients"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f'Sorry, not enough {i} ☹️')
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print('Please insert coins 🪙')
    total = int(input('How many 1€ coins?\n')) * 1
    total += int(input('How many 0,50€ coins?\n')) * 0.5
    total += int(input('How many 0,20€ coins?\n')) * 0.2
    total += int(input('How many 0,10€ coins?\n')) * 0.1
    return total


def transaction_successful(received, drink_cost):
    """Return True when payment accepted. False if insufficient"""
    if received >= drink_cost:
        change = round(received - drink_cost, 2)
        print(f'Here\'s your change: {change}€')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry, not enough money. Coins refunded 🥲')
        return False


def make_coffee(name, order_ingredients):
    """Deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here\'s your {name} ☕️. Enjoy!\n')


is_on = True

while is_on:
    order = input('Hi there!😊 \n Espresso(1,20€) | Latte(2,50€) | Cappuccino(3€)\n What would you like?\n')
    if order == 'off':
        print('Goodbye now!')
        is_on = False
    elif order == 'report':
        print('Here\'s the latest report:')
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: €{profit}")
    elif order not in MENU.keys():
        print('Sorry, we don\'t serve hipsters! Bye now 👋 ')
        is_on = False
    else:
        drink = MENU[order]
        if sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                print('Coming right up!')
                animatron()
                make_coffee(order, drink['ingredients'])
