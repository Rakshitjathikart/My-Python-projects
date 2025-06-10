from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = MenuItem
order = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_on = True
while is_on:
    options = order.get_items()
    choice = input(f"What would you like?({options}) or report: ")
    if choice == "report":
        cm.report()
        mm.report()
    elif choice == "off":
        is_on = False
    else:
        drink = order.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)









