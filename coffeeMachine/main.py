# from menu import MENU
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

# TODO : Print Report

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# sufficient resources
def suff_res(oder_res):
    for item in oder_res:
        if oder_res[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


# Process Coins
def process_coins():
    # print("in money")
    print("Insert Coins: ")
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many Dimes? ")) * 0.1
    total += int(input("How many Nickels? ")) * 0.05
    total += int(input("How many Pennies? ")) * 0.01

    return total


# transaction
def tra_succ(payment, drink_cost):
    # print("in trans")
    if payment >= drink_cost:
        change = round(payment - drink_cost,2)
        print(f"Here's Your change ${change}")

        global money
        money += drink_cost
        return True
    else:
        print("Sorry! not enough money! money refunded!")
        payment = round(payment, 2)
        print(f"Here's Your money ${payment}")
        return False


def makeCoffee(drink_name, order_ing):
    # reduce ingredients from resources
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"Here's Your Coffee {drink_name} ☕️. Enjoy!!")


is_on = True
while is_on:
    order = input("Either wanna report or !What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        is_on = False

    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:
        # print("inside else")
        drink = MENU[order]
        # print(drink)

        # TODO : Check Resources sufficient?
        if suff_res(drink["ingredients"]):

            # TODO : Process Coins
            payment = process_coins()

            # TODO : Check Transaction Successful?
            if tra_succ(payment, drink['cost']):
                makeCoffee(order, drink['ingredients'])

