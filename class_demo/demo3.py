'''
Descripttion:
version:
Author: FF
Date: 2022-12-01 15:16:10
LastEditors: FF
LastEditTime: 2022-12-01 16:08:19
'''
#继承与方法重写
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number

    def __str__(self):
        return 'my name is {0}, the age is {1}'.format(self.name, self.age)

    def info(self):#子类重写了父类的方法，并加入了自己特有的类型
        super().info()
        print(self.number)
class Teacher(Person):
    def __init__(self,name,age,teachoftime):
        super().__init__(name,age)
        self.teachoftime = teachoftime
stu1 = Student('FF',26,'0x005')
stu1.info()
Tea1 = Teacher('lq','36',10)
Tea1.info()

print(stu1) #默认调用__str__方法