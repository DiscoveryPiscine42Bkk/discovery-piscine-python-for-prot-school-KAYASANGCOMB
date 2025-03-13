import sys
x = input('Enter here (separated by spaces and quotes): ')
y = x.split('"')
y = [y.strip() for y in y if y.strip()]
sys.argv.extend(y)
print("Arguments:", y)
print(f'Number of parameters: {len(sys.argv) - 1}')
