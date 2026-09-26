import csv

def write_csv(path='students.csv'):
    rows = [
        ['Name', 'Course', 'Marks'],
        ['Ravi', 'Python', '85'],
        ['Sita', 'Java', '90']
    ]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print('CSV written')

if __name__ == '__main__':
    write_csv()
