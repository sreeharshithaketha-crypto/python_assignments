import json

def read_json(path='student.json'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(data)
    except FileNotFoundError:
        print('JSON not found')

if __name__ == '__main__':
    read_json()
