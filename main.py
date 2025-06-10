from operator import truediv

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

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
}

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total_amt = int(input("How many quarters?:"))*0.25
    total_amt += int(input("How many dimes?:"))*0.10
    total_amt += int(input("How many nickles?:"))*0.05
    total_amt += int(input("How many pennies?:"))*0.01
    return total_amt

def is_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        insufficient_amt = round(drink_cost - money_received, 2)
        print(f"Sorry that's not enough money. You are ${insufficient_amt} short. Money refunded ${money_received}.")

def coffee_making(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) OR Machine report: ")
    if choice == "report":
        print(f"Water:{resources["water"]}")
        print(f"Milk:{resources["milk"]}")
        print(f"Coffee:{resources["coffee"]}")
        print(f"Money:${profit}")
    elif choice == "off":
        is_on =False
    else:
        drink = MENU[choice]
        if is_resource_sufficient(MENU[choice]["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                coffee_making(choice, drink["ingredients"])