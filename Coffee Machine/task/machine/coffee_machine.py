# Write your code here
# First, read the numbers of coffee drinks from the input
# number_coffee_cups = int(input('Write how many cups of coffee you will need:>'))

# inputs
water_in_coffee_machine = input('Write how many ml of water the coffee machine has: ')
milk_in_coffee_machine = input('Write how many ml of milk the coffee machine has: ')
beans_in_coffee_machine = input('Write how many g of beans the coffee machine has: ')
number_coffee_cups = input('Write how many cups of coffee you will need: ')
"""
Figure out how much of each ingredient the machine 
will need. 
Note that one cup of coffee made 
on this coffee machine contains 200 ml of water, 
50 ml of milk, and 15 g of coffee beans.
"""
# coffee amount
cups_amount_water = int(water_in_coffee_machine) / 200
cups_amount_milk = int(milk_in_coffee_machine) / 50
cups_amount_beans = int(beans_in_coffee_machine) / 15
cups_amount_coffee = [cups_amount_water, cups_amount_milk, cups_amount_beans]
# minimum amount of cups of coffee
cups_of_coffee = int(min(cups_amount_coffee))
water = 200 * number_coffee_cups
milk = 50 * number_coffee_cups
beans = 15 * number_coffee_cups
# Output the required ingredient amounts back to the user.
# print('For', number_coffee_cups, 'you will need:')
# print(water, 'ml of water')
# print(milk, 'ml of milk')
# print(beans, 'g of coffee beans')
# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')
# Output is amount of coffee ok
if int(number_coffee_cups) == int(cups_of_coffee):
    print("Yes. I can make that amount of coffee ")
elif int(number_coffee_cups) > int(cups_of_coffee):
    print("No, I can make only", int(cups_of_coffee), "cups of coffee")
else:
    print("Yes, I can make that amount of coffee( and even", int(cups_of_coffee) - int(number_coffee_cups),
          "more than that)")
