def add_student(path='students.txt'):
    name = input('Name: ')
    course = input('Course: ')
    marks = input('Marks: ')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f"{name},{course},{marks}\n")
    print('Student added')

def view_students(path='students.txt'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for record in f:
                name, course, marks = record.strip().split(',')
                print('Name:', name)
                print('Course:', course)
                print('Marks:', marks)
                print('-'*20)
    except FileNotFoundError:
        print('No student records')

if __name__ == '__main__':
    choice = input('1:Add 2:View > ')
    if choice == '1':
        add_student()
    else:
        view_students()
