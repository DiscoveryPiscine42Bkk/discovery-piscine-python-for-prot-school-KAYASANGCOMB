#!/usr/bin/bash python
x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))
z = x * y
print(x, "*", y, "=", z)
if z > 0 : print("The result is positive")
elif z < 0 : print("The result is negative")
elif z == 0 : print("The result is positive and negative")