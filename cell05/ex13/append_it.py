import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a for a in y]
sys.argv.extend(y)
if len(sys.argv) == 1:
    print("none")
else:
    for y in sys.argv[1:]:
        if not y.endswith("ism"):
            print(y + "ism")