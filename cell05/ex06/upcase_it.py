import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a.upper() for a in y]
sys.argv.extend(y)
z = len(sys.argv) - 1
if z == 1:
    print("Arguments:", y)
else: print("none")
