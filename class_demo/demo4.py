'''
Descripttion:
version:
Author: FF
Date: 2022-12-01 16:14:38
LastEditors: FF
LastEditTime: 2022-12-01 16:31:48
'''
#多态
class Animal():
    def eat(self):
        print("动物吃东西")

class Dog(Animal):
    def eat(self):
        print("狗吃狗粮")

class Cat(Animal):
    def eat(self):
        print("猫吃小鱼干")

class Person():
    def eat(self):
        print("人吃动物")

def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Person())