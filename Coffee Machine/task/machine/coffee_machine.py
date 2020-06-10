# Write your code here
# First, read the numbers of coffee drinks from the input
# number_coffee_cups = int(input('Write how many cups of coffee you will need:>'))
water = 400
milk = 540
coffee_beans = 120
disposible_cups = 9
money = 550
balance_espresso_water = 250
balance_espresso_coffee_bean = 16
balance_espresso_money = 4
balance_latte_water = 350
balance_latte_milk = 75
balance_latte_coffee_beans = 20
balance_latte_money = 7
balance_cappuccino_water = 200
balance_cappuccino_milk = 100
balance_cappuccino_coffee_beans = 12
balance_cappuccino_money = 6


def take():
    # money = money - money
    print("I gave you: $", money)
    print(" ")
    print(" ")
    print("The coffee machine has:")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(coffee_beans, "g of coffee beans")
    print(disposible_cups, "of disposable cups")
    print(money - money, "$ of money")


def fill():
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many of milk do you want to add: "))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    print("The coffee machine has: ")
    print(water + add_water, "ml of water")
    print(milk + add_milk, " ml of milk")
    print(coffee_beans + add_coffee_beans, "g of coffee beans")
    print(disposible_cups + add_cups, "of disposable cups")
    print(money, "of money")


def buy():
    choise_type_coffee = int(input("What do you wont to buy 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if choise_type_coffee == 1:
        print("The coffee machine has: ")
        print(water - balance_espresso_water, "ml of water")
        print(milk, "ml of milk")
        print(coffee_beans - balance_espresso_coffee_bean, "g of coffee beans")
        print(disposible_cups - 1, "disposable cups ")
        print(money + balance_espresso_money, "$ of money")
    elif choise_type_coffee == 2:
        print("The coffee machine has: ")
        print(water - balance_latte_water, "ml of water")
        print(milk - balance_latte_milk, "ml of milk")
        print(coffee_beans - balance_latte_coffee_beans, "g of coffee beans")
        print(disposible_cups - 1, "of disposable cups")
        print(money + balance_latte_money, "$ of money")
    elif choise_type_coffee == 3:
        print("The coffee machine has: ")
        print(water - balance_cappuccino_water, "ml of water")
        print(milk - balance_cappuccino_milk, "ml of milk")
        print(coffee_beans - balance_cappuccino_coffee_beans, "g of coffee beans")
        print(disposible_cups - 1, "of disposable cups")
        print(money + balance_cappuccino_money, "$ of money")


print(" The coffee machine has: ")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(disposible_cups, "of disposable cups")
print(money, "of money")
print(" ")
choise_type_action: str = str(input("Write action (buy, fill, take): "))
# while choise_type_action in list['buy', 'fill', 'take']:
if choise_type_action == 'take':
    take()

elif choise_type_action == "fill":
    fill()
else:
    buy()
# # inputs
# water_in_coffee_machine = input('Write how many ml of water the coffee machine has: ')
# milk_in_coffee_machine = input('Write how many ml of milk the coffee machine has: ')
# beans_in_coffee_machine = input('Write how many g of beans the coffee machine has: ')
# number_coffee_cups = input('Write how many cups of coffee you will need: ')
# """
# Figure out how much of each ingredient the machine
# will need.
# Note that one cup of coffee made
# on this coffee machine contains 200 ml of water,
# 50 ml of milk, and 15 g of coffee beans.
# """
# # coffee amount
# cups_amount_water = int(water_in_coffee_machine) / 200
# cups_amount_milk = int(milk_in_coffee_machine) / 50
# cups_amount_beans = int(beans_in_coffee_machine) / 15
# cups_amount_coffee = [cups_amount_water, cups_amount_milk, cups_amount_beans]
# # minimum amount of cups of coffee
# cups_of_coffee = int(min(cups_amount_coffee))
# water = 200 * number_coffee_cups
# milk = 50 * number_coffee_cups
# beans = 15 * number_coffee_cups
# # Output the required ingredient amounts back to the user.
# # print('For', number_coffee_cups, 'you will need:')
# # print(water, 'ml of water')
# # print(milk, 'ml of milk')
# # print(beans, 'g of coffee beans')
# # print('Starting to make a coffee')
# # print('Grinding coffee beans')
# # print('Boiling water')
# # print('Mixing boiled water with crushed coffee beans')
# # print('Pouring coffee into the cup')
# # print('Pouring some milk into the cup')
# # print('Coffee is ready!')
# # Output is amount of coffee ok
# if int(number_coffee_cups) == int(cups_of_coffee):
#     print("Yes. I can make that amount of coffee ")
# elif int(number_coffee_cups) > int(cups_of_coffee):
#     print("No, I can make only", int(cups_of_coffee), "cups of coffee")
# else:
#     print("Yes, I can make that amount of coffee( and even", int(cups_of_coffee) - int(number_coffee_cups),
#           "more than that)")
