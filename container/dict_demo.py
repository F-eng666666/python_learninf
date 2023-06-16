import copy

#字典的创建
dict1 = {'name': 'Tom', 'age': 18}
print(f"dict1字典为{dict1}")
dict1 = dict(name='Tony', age=19)
print(f"dict1字典为{dict1}")

#
#采用直接的赋值是浅拷贝,指向同一个对象
dict1_1 = dict1
print(f"dict1_1字典为{dict1_1}")
dict1['age'] = 66
print(f"dict1字典修改,dict1_1也会被修改:{dict1_1}")
#如果采用使用copy的方法进行复制,会指向不同的对象
dict1_2 = dict1.copy()
print(f"dict1_2字典为{dict1_2}")
dict1['age'] = 100
dict1_2['name'] = 'Alice'
print(f"dict1字典修改,dict1_2也会被修改:{dict1}")
print(f"采用copy的方法,dict1字典修改,dict1_2不会被修改:{dict1_2}")

#字典的修改
dict2 = {'name': 'Alice', 'age': 25, 'gender': 'female'}
dict2['age'] = 66
print(f"修改一个已经存在的键值dict2字典为{dict2}")
#当修改一个不存在的值时,相当于添加新的键值对
dict2['city'] = 'shanghai'
print(f"修改一个不存在的键值dict2字典为{dict2}")
#采用update方法进行修改,存在的修改,不存在的创建
dict2.update({'age':18, 'hobby':'python'})
print(f"dict2字典为{dict2}")

#字典的复制
#1.直接使用"="对字典进行复制,原字典的地址直接赋值给新的变量,基本数据类型和引用数据类型都共用一份
dict3 = {1: 'one', 2: 'two', 3: [1, 2, 3]}
dict3_1 = dict3.copy()
dict3[1] = 'oneone'
print(f"dict3字典为{dict3}")
print(f"dict3_1字典为{dict3_1}")

#2.使用copy方法对字典进行浅拷贝复制,基本数据类型独立,引用数据类型共用一份
dict3 = {1: 'one', 2: 'two', 3: [1, 2, 3]}
dict3_1 = dict3.copy()
#dict3_1 = copy.copy(dict3)
dict3[3][0] = 4
dict3_1[1] = 'oneone'
print(dict3)  # 输出: {1: 'one', 2: 'two', 3: [4, 2, 3]}
print(dict3_1)  # 输出: {1: 'oneone', 2: 'two', 3: [4, 2, 3]}

#使用copy.deepcopy(dict3)的方法对字典进行深拷贝时,基本和引用都独立
dict3 = {1: 'one', 2: 'two', 3: [1, 2, 3]}
dict3_1 = copy.deepcopy(dict3)
dict3_1[3][0] = 55555
print(dict3)  # 输出: {1: 'one', 2: 'two', 3: [4, 2, 3]}
print(dict3_1)  # 输出: {1: 'one', 2: 'two', 3: [5, 2, 3]}