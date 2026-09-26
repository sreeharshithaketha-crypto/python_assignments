def copy_file(src='source.txt', dst='destination.txt'):
    try:
        with open(src, 'r', encoding='utf-8') as s:
            data = s.read()
        with open(dst, 'w', encoding='utf-8') as d:
            d.write(data)
        print('Copied')
    except FileNotFoundError:
        print('Source not found.')

if __name__ == '__main__':
    copy_file()
