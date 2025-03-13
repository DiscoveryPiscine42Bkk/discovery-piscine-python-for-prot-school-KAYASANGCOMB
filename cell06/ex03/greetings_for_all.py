def greetings(y="noble stranger"):
    if not y.replace(" ", "").isalpha():
        print("Error: That is not a name")
    else:
        print(f"Welcome, {y}!")
if __name__ == "__main__":
    x = input("Enter your name (or press Enter to skip): ").strip()
    if x == "":
        greetings()
    else:
        greetings(x)
input()