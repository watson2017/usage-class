#!/usr/bin/env python
# coding=utf-8
"""
    文档结构说明:
    ①本文档中包含两个大类，一是Dog类，较为简单；二是，car类；car 类型包含内容分为，父类、子类的继承与重定义、类中的调用等内容
    ②car类单独写到了另外一个car.py文件，通过from 进行调用
"""

from car import ElectricCar, Car


# ===============================例子：Dog 类==============================
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("my dog " + self.name.title() + " is now sitting")


my_dog = Dog('apple', 6)
# my_dog.name 获取类的name参数
print("my dog's name is " + my_dog.name.title())  # title 将首字母大写
print("my dog is " + str(my_dog.age) + " years old")
# 使用类中sit方法
my_dog.sit()
# ===========================================================================

my_car = Car('benci', 'hhhh', 2017)
elc_car = ElectricCar('aodi', 'yy', 2018)
print(my_car.get_descriptive_name())
print(elc_car.get_descriptive_name())
elc_car.read_odometer()
# my_car.odometer_reading = 50
my_car.update_odometer(50)
my_car.read_odometer()
elc_car.battery.describe_battery()  # 调用3中的battery类