def create_file(path='myinfo.txt'):
    name = input('Name: ')
    course = input('Course: ')
    city = input('City: ')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"{name}\n{course}\n{city}\n")
    print('File created:', path)

if __name__ == '__main__':
    create_file()
