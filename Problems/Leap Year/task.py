check_year = int(input())
while 1900 <= check_year <= 3000:
    devisible_4 = check_year % 4
    devisible_100 = check_year % 100
    devisible_400 = check_year % 400
    if devisible_4 == 0 and devisible_100 != 0 or devisible_400 == 0:
        print("Leap")
        break
    print("Ordinary")
    break
else:
    print("Wrong Year")
