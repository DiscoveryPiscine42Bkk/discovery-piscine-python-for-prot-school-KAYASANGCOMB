x = input('Enter here: ')
y = x.split()
print("Arguments:", y)
if len(y) > 0 :
    print(f'First parameters:', {y[0]})
else : print('none')