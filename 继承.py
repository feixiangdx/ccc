import time


# class OldPhone:
#     __brand = ""
#
#     def setBrand(self, brand):
#         self.__brand = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def callPhone(self, username):
#         print(f"正在给{username}打电话")
#
#
# # o = OldPhone()
# # o.callPhone("齐馨")
#
# class NewPhone(OldPhone):
#     def callPhone(self, username):
#         print("语音拨号中", end="")
#         for i in range(3):
#             time.sleep(1)
#             print(".", end="")
#         print()
#         super().callPhone(username)
#
#     def goodPhone(self):
#         print("品牌为：", self.getBrand(), "的手机很好用")
#
#
# n = NewPhone()
# n.setBrand(input("请输入手机品牌："))
# n.callPhone(input("请输入拨打对象："))
# n.goodPhone()


# class OldCook:
#     __name = ""
#     __age = ""
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def rice(self):
#         print(self.__name, "正在蒸饭")
#
#
# class NewCook(OldCook):
#     def cai(self):
#         print(self.getAge(), "正在炒菜")
#
#
# class Cookl(NewCook):
#     def rice(self):
#         print("蒸饭")
#
#     def cai(self):
#         print("炒菜")
#
#     def text(self):
#         print(self.getName(), self.getAge())
#
#
# a = Cookl()
# a.setName(input("请输入姓名："))
# a.setAge(input("请输入年龄："))
# a.rice()
# a.cai()
# a.text()


class Person:
    __name = ""
    __age = ""
    __sex = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex

    def getName(self):
        return self.__sex


class Work(Person):
    def addwork(self):
        print("干活")


w = Work()
w.setName(1)
w.setAge(1)
w.setSex(1)
w.addwork()


class Student(Person):
    __id = ""

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def study(self):
        print("学习")

    def song(self):
        print("唱歌")


s = Student()
s.setName(1)
s.setAge(1)
s.setSex(1)
s.setId(1)
s.study()
s.song()
