#!/usr/bin/python3
x = float(input("Enter a number less than 25 : "))
if x < 25:
    while x < 26:
        print(x)
        if x == 25:
            break
        x += 1
elif x >= 25 : print("Error, That's not less than 25. Stupid.")