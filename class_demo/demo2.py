#类的封装
class Student(object):
    def __init__(self,name,age,number):
        self.name = name
        self.number = number
        self.__age = age    #age不希望在外部使用，所以加了两个__，只是不希望
    def printinfo(self):
        print("age is " + str(self.__age))


stu1= Student('ff',26,66)
print(dir(stu1)) #输出对象可以使用的所有方法和属性
print(stu1.name)
print(stu1.number)
#print(stu1.__age) #加了两个__后不能在和之前没有加连个__的时候一样使用
print(stu1._Student__age) #强行使用的方法，君子协议
stu1.printinfo()

