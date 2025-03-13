def decimal(value):
    try:
        x = float(value)
        return x != int(x)
    except:
        return False
    
y = input("Enter the number: ")

if decimal(y):
    print("This number is a decimal")
else:
    print("This number is an integer")