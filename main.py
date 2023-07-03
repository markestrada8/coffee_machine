import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "bank": 1.40
}

user_input = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 1. PRINT REPORT
if user_input == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Funds: {locale.currency(float(resources['bank']))}")

elif user_input == "off":
    exit()

else:
    # TODO: 2.  CHECK SUFFICIENT RESOURCES
    if MENU[user_input]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water")
    if MENU[user_input]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk")
    if MENU[user_input]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee")

    # TODO: 3.  PROCESS COINS
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    # TODO: 4.  CHECK TRANSACTION SUCCESSFUL
    total = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    if total < MENU[user_input]["cost"]:
        print("Sorry, that's not enough money. Money refunded")
    else:
        # TODO: 5.  MAKE COFFEE
        # TODO: 6.  DEDUCT RESOURCES
        change = total - MENU[user_input]["cost"]
        resources["bank"] += total - change
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        print(f"Here is {locale.currency(round(change, 2))} dollars in change")
        print(f"Here is your {user_input}. Enjoy!")



