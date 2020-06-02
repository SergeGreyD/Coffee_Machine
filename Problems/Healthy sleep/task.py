sleep_per_dey_min = input()
sleep_per_day_max = input()
sleep_per_day_real = input()
if int(sleep_per_day_real) < int(sleep_per_dey_min):
    print("Deficiency")
elif int(sleep_per_day_real) > int(sleep_per_day_max):
    print("Excess")
else:
    print("Normal")
