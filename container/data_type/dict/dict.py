#字典的相关操作

dict1={'abc':456}
dict2={'abc':123,96.3:37}
print(dict1)
print(dict2)

dict3=dict()#创建空字典
dict4=dict(a='a23',b='b45',c='c78')#传入关键字
dict5=dict(zip(['one','two','three'],[1,2,3])) #映射函数
dict6=dict([('one',1),('two',2),('three',3)])#可迭代对象方式构建字典
print(dict3)
print(dict4)
print(dict5)
print(dict6)

#字典的访问
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict['Name'])
print(dict['Age'])

#字典的遍历
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for key in dict:
    print(f'key={key},value={dict[key]}')

#修改字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Name']='Jennifer' #修改
dict['School']='ABCuniversity' #添加
print(dict)

#删除元素
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] #删除键是’Name‘的条目
print(dict)
dict.clear()#清空字典的所有条目
print(dict)
del dict

#if 判断
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
if 'Name'in dict:
    print(True)
if 'Namelala' not in dict:
    print(True)

#分类
dict = {1:2,3:4,5:6}
key=dict.keys()
print(sorted(key))
value=dict.values()
print(sorted(value))
items=dict.items()
print(sorted(items))

#字典连接函数 update（）
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
dict2={'sex':'male','School':'abcuniversity2','Class':3}
dict.update(dict2)
print(dict)

#字典的copy
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2=dict.copy()
print(dict2)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
key=dict.keys()
value=dict.values()
print(type(key))
print(type(value))
print(value)
print(key)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
key_value = list(dict.keys())
value_list = list(dict.values())

print(key_value)
print(value_list)


"""
#字典里套列表
dic1 = {}
#dic1.setdefault(key,[]).append(value)
dic1.setdefault('a',[]).append(1)
dic1.setdefault('a',[]).append(2)
print(dic1)

#字典里套字典
dic2 = {}
#dic.setdefault(key,{})[value] =1
dic2.setdefault('b',{})['f']=1
dic2.setdefault('b',{})['h']=1
dic2.setdefault('b',{})['g']=1
print(dic2)
"""