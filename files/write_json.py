import json

def write_json(path='student.json'):
    student = {'name':'Ravi','course':'Python','marks':85}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(student, f, indent=2)
    print('JSON written')

if __name__ == '__main__':
    write_json()
