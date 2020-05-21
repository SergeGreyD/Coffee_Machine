# put your python code here
first_numeber = input()
second_number = input()
operator = input()
prohibited_operators = ['/', 'mod', 'div']
if float(second_number) == 0 and operator in prohibited_operators:
    print("Division by 0!")
elif operator == '+':
    print(float(first_numeber) + float(second_number))
elif operator == '*':
    print(float(first_numeber) * float(second_number))
elif operator == '-':
    print(float(first_numeber) - float(second_number))
elif operator == '/':
    print(float(first_numeber) / float(second_number))
elif operator == 'mod':
    print(float(first_numeber) % float(second_number))
elif operator == 'pow':
    print(float(first_numeber) ** float(second_number))
elif operator == 'div':
    print(float(first_numeber) // float(second_number))
