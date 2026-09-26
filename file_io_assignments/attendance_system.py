from datetime import datetime

def mark_attendance(path='attendance.txt'):
    name = input('Student name: ')
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%I:%M %p')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f"{name},{date},{time},Present\n")
    print('Recorded')

if __name__ == '__main__':
    mark_attendance()
