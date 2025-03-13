def main():
    x = input("Enter two numbers separated by space: ").split()
    if len(x) != 2:
        print("none")
        return
    try:
        num1 = int(x[0])
        num2 = int(x[1])
    except ValueError:
        print("none")
        return
    result_array = list(range(num1, num2 + 1))
    print(result_array)
main()