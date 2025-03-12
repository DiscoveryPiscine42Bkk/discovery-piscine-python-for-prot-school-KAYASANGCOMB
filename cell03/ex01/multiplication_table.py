#!/usr/bin/python3
x = float(input("Enter a number : "))
y = 0
while y < 13:
    z = x * y
    print(x, "*", y, "=", z)
    if y == 12:
        break
    y += 1