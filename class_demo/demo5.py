'''
Descripttion:
version:
Author: FF
Date: 2022-12-01 16:40:26
LastEditors: FF
LastEditTime: 2022-12-01 16:44:05
'''
#类的特殊属性和方法
a=10
b=100
c=a+b
c=a.__add__(b)
print(c)


class  Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name

stu1  = Student('张三')
stu2 = Student('李四')
print(stu1+stu2)