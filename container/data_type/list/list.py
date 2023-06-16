from collections import Counter






#列表的扩展
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]
#1、apend
list_1.append(list_2)
print(list_1)
#2.extend
list_2.extend(list_3)
print(list_2)
#3.insert
number=[1,2,4,5]
number.insert(2,3)
print(number)

#查找对象的索引值
number=[1,2,3,4,5,6,7,8,9,10,11,'3']
print(number)
print(number.index(3))
print(number.index('3'))

#统计指定元素的个数
# 随便定义一个list，也可以是自己生成的
temp = [1, 2, 1, 3, 4, 2, 3, 6, 3]
count = Counter(temp)
print(count)
# 输出元素3的个数
print(count[3]) 

#测试list长度
print(len(temp))