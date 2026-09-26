def count_words_chars(path='article.txt'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        words = content.split()
        print('Words:', len(words))
        print('Characters:', len(content))
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    count_words_chars()
