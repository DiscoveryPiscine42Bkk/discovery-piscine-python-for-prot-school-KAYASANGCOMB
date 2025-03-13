import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip().upper() for item in x.split('"') if item.strip()]
y = [a.lower() for a in y]
sys.argv.extend(y)
z = len(sys.argv) - 1
if z > 0:
    print("Arguments:", y)
else: print("none")
