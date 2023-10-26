num = int(input("How many numbers ?"))
total = 0

for n in range (num):
    numbers = float(input("Give me a number"))
    total += numbers

average = total / num

print(f"Average is : {average}")