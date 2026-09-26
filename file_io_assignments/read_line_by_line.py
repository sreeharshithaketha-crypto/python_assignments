def read_lines(path='courses.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

if __name__ == '__main__':
    read_lines()
