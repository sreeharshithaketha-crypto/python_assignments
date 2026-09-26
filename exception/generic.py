try:
    num = int(input("Enter a number: "))
    print(100 / num)
except Exception as error:
    print("Error:", error)