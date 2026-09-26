def search_word(path='article.txt'):
    word = input('Search word: ').strip().lower()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        print('Found' if word in content else 'Not found')
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    search_word()
