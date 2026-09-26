def replace_word(path='article.txt'):
    old = input('Old word: ')
    new = input('New word: ')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Replaced')
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    replace_word()
