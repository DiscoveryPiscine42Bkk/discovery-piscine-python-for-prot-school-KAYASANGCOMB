def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string.ljust(8, 'Z'))

def main():
    user_input = input("Enter a string(or multiple strings separated by spaces): ")
    strings = user_input.split()
    if len(strings) < 1:
        print("none")
    else:
        for string in strings:
            if len(string) > 8:
                shrink(string)
            elif len(string) < 8:
                enlarge(string)
            else:
                print(string)

if __name__ == "__main__":
    main()