import sys
def downcase(txt):
    return txt.lower()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("none")
    else:
        for arg in sys.argv[1:]:
            print(downcase(arg))
input()