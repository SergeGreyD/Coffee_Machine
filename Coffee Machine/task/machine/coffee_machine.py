# Write your code here
# First, read the numbers of coffee drinks from the input
number_coffee_cups = int(input('Write how many cups of coffee you will need:>'))
"""
Figure out how much of each ingredient the machine 
will need. 
Note that one cup of coffee made 
on this coffee machine contains 200 ml of water, 
50 ml of milk, and 15 g of coffee beans.
"""
water = 200 * number_coffee_cups
milk = 50 * number_coffee_cups
beans = 15 * number_coffee_cups
# Output the required ingredient amounts back to the user.
print('For', number_coffee_cups, 'you will need:')
print(water, 'ml of water')
print(milk, 'ml of milk')
print(beans, 'g of coffee beans')
# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')
