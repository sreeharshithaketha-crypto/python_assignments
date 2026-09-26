def update_line(path='article.txt'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        n = int(input('Line number to update: '))
        text = input('New text: ') + '\n'
        if 1 <= n <= len(lines):
            lines[n-1] = text
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print('Updated')
        else:
            print('Invalid line number')
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    update_line()
