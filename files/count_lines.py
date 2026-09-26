def count_lines(path='students.txt'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            print(sum(1 for _ in f))
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    count_lines()
