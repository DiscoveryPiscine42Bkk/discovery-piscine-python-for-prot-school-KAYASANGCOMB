import sys
x = input('Enter here (separated by quotes): ')
y = [item.strip() for item in x.split('"') if item.strip()]
y = [a for a in y]
sys.argv.extend(y)
if len(sys.argv) != 2:
    print("none")
else:
    y = sys.argv[1]
    x = input("Enter a word: ")
    if x == y:
        print("Good job!")
    else:
        print("Nope, sorry...")