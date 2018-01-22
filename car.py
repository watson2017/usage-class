# ================================1.car 的父类================================
class Car():
    def __init__(self, make, model, years):
        """make:生产商，model：型号，years：生产年限"""
        self.make = make
        self.model = model
        self.years = years
        self.odometer_reading = 0  # 设置一个参数，汽车跑的总里程数，初始值为0，无需外界传入

    def get_descriptive_name(self):
        long_name = str(self.years) + ',' + self.model + ',' + self.make
        return long_name.title()

    def read_odometer(self):
        # self.odometer_reading = 23
        print("this car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, newmiles):
        """
            将里程表读数设定为指定的值
            禁止将里程表的读数往回拨
        """
        # self.odometer_reading = newmiles
        if self.odometer_reading <= newmiles:
            self.odometer_reading = newmiles
        else:
            print("you can not rollback an old meter !")


# ======================2.子类的创建======================================
# 创建子类时，父类必须包含在当前文件中，且位于子类前面
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值
# super()是一个特殊函数，帮助Python将父类和子类关联起来
# =========================================================================
class ElectricCar(Car):  # 括号中object表示从哪里继承父类
    def __init__(self, make, model, years):
        super().__init__(make, model,
                         years)  # 继承父类的属性(其中的方法)，与Python2 版本中写法不一样
        self.battery = Battery(66)  # 调用Battery类

    def read_odometer(self):
        """重写父类的方法：在子类中定义一个与要重写的父类方法同名。这样，Python就不会继承这个父类方法"""
        print("elc car not need read miles.")


# ============================3.将实例用作属性==================================
# 将类的一部分作为一个独立的类提取出来，可以将大型类拆分成多个协同工作的小类
# 如下方的Battery实例可以用作ElectricCar类的一个属性
# ==============================================================================
class Battery():
    def __init__(self, battery_size=100):
        """初始化电池的容量"""
        self.battery_size = battery_size

    def describe_battery(self):
        """描述电池剩余量"""
        print("this electriccar has a " + str(self.battery_size) +
              " -kWh battery.")
