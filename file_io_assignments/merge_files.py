def merge_files(file1='file1.txt', file2='file2.txt', out='merged.txt'):
    try:
        with open(file1, 'r', encoding='utf-8') as f1:
            c1 = f1.read()
        with open(file2, 'r', encoding='utf-8') as f2:
            c2 = f2.read()
        with open(out, 'w', encoding='utf-8') as o:
            o.write(c1 + '\n' + c2)
        print('Merged into', out)
    except FileNotFoundError as e:
        print('File not found:', e)

if __name__ == '__main__':
    merge_files()
