x = input('Enter here: ')
y = x.split()
print("Arguments:", y)
if len(y) > 2 :
    print("Arguments in reverse order:")
    for z in reversed(y):
        print(z)
else : print('none')