import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a for a in y]
sys.argv.extend(y)
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    count = string.count(keyword)
    if count > 0:
        print(count)
    else:
        print("none")