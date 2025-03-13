import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a for a in y]
sys.argv.extend(y)
if len(sys.argv) != 2:
    print("none")
else:
    str = sys.argv[1]
    z_count = str.count("z")
    if z_count == 0:
        print("none")
    else:
        for _ in range(z_count):
            print("z")