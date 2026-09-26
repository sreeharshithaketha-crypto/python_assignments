def read_file(path='myinfo.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == '__main__':
    read_file()
