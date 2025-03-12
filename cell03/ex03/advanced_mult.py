x = 0
while x <= 12:
    y = 1
    while y <= 12:
        z = x * y
        print(f"{x} * {y} = {z}")
        y += 1
    print()
    x += 1