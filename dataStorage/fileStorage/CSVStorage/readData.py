import csv

with open('data.csv', 'r', encoding='utf8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
