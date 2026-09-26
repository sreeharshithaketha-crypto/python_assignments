try:
    fname = input("Enter filename: ")
    with open(fname, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist.")
