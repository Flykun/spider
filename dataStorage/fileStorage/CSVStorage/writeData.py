import csv

with open('data1.csv', 'w') as csv_file:
    write = csv.writer(csv_file, delimiter=' ')
    write.writerow(['id', 'name', 'age'])
    write.writerow(['10001', 'Mike', '20'])
    write.writerow(['10002', 'Bob', '21'])
    write.writerow(['10003', 'Jordan', '22'])

with open('data2.csv', 'w') as csv_file:
    fieldnames = ['id', 'name', 'age']
    write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    write.writeheader()
    write.writerow({'id': '10001', 'name': 'Mike', 'age': '20'})
    write.writerow({'id': '10002', 'name': 'Bob', 'age': '21'})
    write.writerow({'id': '10003', 'name': 'Jordan', 'age': '22'})
