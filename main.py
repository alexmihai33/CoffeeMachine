from machine_utilities import MENU, resources


def report():
    """"Prints the machine resources"""
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {resources["money"]}")


def order_resource_check(coffee_type):
    """Check resources availability for certain coffe"""
    for resource in coffee_type["ingredients"]:
        if coffee_type["ingredients"][resource] > resources[resource]:
            print(f"There is not enough {resource}")
            return False
        else:
            return True


def money_insert():
    """Returns the total amount of money inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
    return total


def order_money_check(money_placed, coffee_cost):
    """Prints change and returns True if there is enough money"""
    if money_placed >= coffee_cost:
        change = round(money_placed-coffee_cost, 2)
        print(f"Your change: ${change}")
        return True
    else:
        print("Not enough money inserted")
        return False


def order_resources_change(coffee_type):
    """"Changing resources if order was placed"""
    resources["water"] -= coffee_type["ingredients"]["water"]
    resources["milk"] -= coffee_type["ingredients"]["milk"]
    resources["coffee"] -= coffee_type["ingredients"]["coffee"]
    resources["money"] += coffee_type["cost"]


machine_is_on = True


while machine_is_on:
    input_validation = False
    user_input = ""
    while not input_validation:
        user_input = input('What would you like? Type your choice: espresso/latte/cappuccino/report/off ')
        # report - outputs machine resources
        # off - turns the machine off
        if user_input != "espresso" and user_input != "latte" and user_input != "cappuccino" and user_input != "report" and user_input != "off":
            print("Please type valid input")
        else:
            input_validation = True
    if user_input == "off":
        machine_is_on = False
    elif user_input == "report":
        report()
    else:
        if order_resource_check(MENU[user_input]):
            money_inserted = money_insert()
            if order_money_check(money_inserted, MENU[user_input]["cost"]):
                print(f"Enjoy your {user_input}")
                order_resources_change(MENU[user_input])
