def delete_line(path='article.txt'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        n = int(input('Line number to delete: '))
        if 1 <= n <= len(lines):
            del lines[n-1]
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print('Deleted')
        else:
            print('Invalid line number')
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    delete_line()
