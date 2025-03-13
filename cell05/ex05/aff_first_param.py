import sys
x = input('Enter here (separated by spaces and quotes): ')
y = x.split('"')
y = [y.strip() for y in y if y.strip()]
sys.argv.extend(y)
print("Arguments:", y)
z = len(sys.argv) - 1
if z > 0:
    print(y[0])
else: print("none")
