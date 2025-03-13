import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a for a in y]
sys.argv.extend(y)
y.reverse()
z = len(sys.argv) - 1
if z >= 2:
    print("Arguments(Reversed):", y)
else: print("none")
