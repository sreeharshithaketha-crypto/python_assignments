def append_course(path='courses.txt'):
    course = input('Course to append: ')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(course + '\n')
    print('Appended.')

if __name__ == '__main__':
    append_course()
