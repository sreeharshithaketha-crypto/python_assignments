try:
    number = 100
    number.append(200)
except AttributeError:
    print("Integer objects do not have an append method.")