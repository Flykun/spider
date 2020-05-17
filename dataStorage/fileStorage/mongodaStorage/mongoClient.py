import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.text  # client['text']
collection = db.students
# 增加数据
# insert_one(), insert_many()
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)

# 查询数据
# find_one()  查询得到单个结果
result = collection.find_one({'name': 'Mike'})
print(result)

# 查询多个数据

results = collection.find()
for result in results:
    print(result)

# 计数
count = collection.find().count()
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移
# skip()  忽略前两个数据
# limit()  限制查询数据
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 更新
# 官方不推荐update(), 推荐使用update_one(), update_many()
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

# 删除
# remove()
result = collection.remove({'name': 'Kevin'})
print(result)