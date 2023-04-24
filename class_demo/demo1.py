'''
Descripttion:
version:
Author: sueRimn
Date: 2022-11-28 08:12:13
LastEditors: FF
LastEditTime: 2022-12-01 14:48:28
'''
class Student:
    native_pace = '菏泽' #直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name = name #self.name称为实体属性，进行了一个赋值操作，将局部变量的name的值赋给实体属性
        self.age = age

    #实例方法
    def eat(self):
        print(self.native_pace)
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def method():
        print('这是一个静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')



#在类内定义的称为方法，在类之外定义的称为函数

print(id(Student))   #开辟了内存空间
print(type(Student)) #类型是一个类
print(Student)

print('`````````````````````````')
#使用类创建一个对象
stu1 = Student('张三',11)
print(id(stu1))   #开辟了内存空间
print(type(stu1)) #类型是一个类
print(stu1)       #所处内存地址

print('`````````````````````````')
#属性、方法的调用
print(stu1.name)
print(stu1.native_pace)
stu1.eat()          #通过对象名.方法名（）调用
Student.eat(stu1)   #类名.方法名（类的对象），实际上就是方法定义处的self

#类属性调用
stu2 = Student('李四',20)
print(stu1.native_pace)
print(stu2.native_pace)

print('```````````````````````')
Student.native_pace = "山东" #全部对象都被修改
print(stu1.native_pace)
print(stu2.native_pace)

print('````````````````````````')
stu1.native_pace = "北京"    #仅仅修改了对应的对象
print(stu1.native_pace)
print(stu2.native_pace)


print('----------类方法使用----------------')
Student.cm()
print('----------静态方法使用----------------')
Student.method()

print("--------------动态绑定-----------------")
print("------------------动态绑定属性----------")
stu1.gender = "female"
print(stu1.gender)
#print(stu2.gender),会报错

print("------------------动态绑定方法----------")
print(dir(stu1)) #输出对象可以使用的所有方法和属性
def show():
    print("动态绑定方法")
stu1.show = show
stu1.show()
print(dir(stu1)) #输出对象可以使用的所有方法和属性