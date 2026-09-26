import csv

def read_csv(path='students.csv'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print('CSV not found')

if __name__ == '__main__':
    read_csv()
