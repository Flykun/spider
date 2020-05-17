import pymysql

# # 创建数据库
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print(f'Database version: ', data)
#
# # 创建表
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# # 插入数据
# id = '20120001'
# user = 'Bob'
# age = 20
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)' # 使用(%s, 替代)
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback() # 意外回滚
# db.close()

# # 另一种插入方法
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}{keys} VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#     cursor.execute(sql, tuple(data.values()))
#     print('成功')
#     db.commit()
# except:
#     print('失败')
#     db.rollback() # 意外回滚
# db.close()

# # 更新数据
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     print('成功')
#     db.commit()
# except:
#     db.rollback()
#     print('失败')
# db.close()

# 更灵活的更新方式, 字典传值, 如果主键存在, 就更新, 而不是插入
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = f'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())* 2):
        print('成功')
        db.commit()
except:
    db.rollback()
    print('失败')
db.close()

# 删除数据
table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
# 查询数据
sql = 'SELECT * FROM students WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')