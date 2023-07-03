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
    "bank": 0
}


def print_report():
    """Print report of resources and return NONE"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Funds: {locale.currency(float(resources['bank']))}")


def sufficient_resources(choice):
    """Receive user choice: STR and return result of resource check: BOOL"""
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water")
        return False
    elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk")
        return False
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True


def process_coins():
    """return coin amount input: INT"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters, dimes, nickels, pennies


def process_transaction(quarters, dimes, nickels, pennies):
    """Process payment, return result text: STR"""
    total = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    if total < MENU[user_input]["cost"]:
        return "Sorry, that's not enough money. Money refunded"
    else:
        # TODO: 5.  MAKE COFFEE
        # TODO: 6.  DEDUCT RESOURCES
        change = total - MENU[user_input]["cost"]
        resources["bank"] += total - change
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        if change:
            print(f"Here is {locale.currency(round(change, 2))} dollars in change")
        return f"Here is your {user_input}. Enjoy!"


on = True

# Program Loop
while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 1. PRINT REPORT
    if user_input == "report":
        print_report()

    elif user_input == "off":
        on = False

    else:
        # TODO: 2.  CHECK SUFFICIENT RESOURCES
        if sufficient_resources(user_input):
            # TODO: 3.  PROCESS COINS
            quarters, dimes, nickels, pennies = process_coins()

            # TODO: 4.  CHECK TRANSACTION SUCCESSFUL
            print(process_transaction(quarters, dimes, nickels, pennies))
