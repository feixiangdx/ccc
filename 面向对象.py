'''
    1、杯子进行面向对象，定义属性，定义方法
    2、杯子的正常属性需隐藏,进行取值和赋值
    3、属性的正常形式，判断

'''


class cub:
    __high = ""
    __bulk = ""
    __color = ""
    __Material = ""

    def sethigh(self, high):

        if high < 0:
            print("请正确输入高度，你见过这样的杯子吗？笨！！！！！！！")
            c.sethigh(int(input("请输入杯子高度：")))
        else:
            self.__high = high

    def gethigh(self):
        return self.__high

    def setbulk(self, bulk):
        if bulk < 0:
            print("你们家杯子是一面镜子吗?????")
        else:
            self.__bulk = bulk

    def getbulk(self):
        return self.__bulk

    def setcolor(self, color):
        self.__color = color

    def getcolor(self):
        return self.__color

    def setMaterial(self, material):
        self.__Material = material

    def getMaterial(self):
        return self.__Material

    def save(self):
        print("这个杯子是", self.__high, "厘米高", "容积为", self.__bulk, "ml", "存放", self.__color, "颜色",
              self.__Material, "的杯子")


c = cub()
c.sethigh(int(input("请输入杯子高度：")))
c.setbulk(int(input("请输入杯子容积：")))
c.setcolor(input("请输入液体颜色："))
c.setMaterial(input("请输入液体名称："))
c.save()

print("--------------------------------------------------------------------------------------------")

'''
    1、电脑配置，用途
    2、一些配置要符合基本需求
    
    
'''


class computer:
    __size = ""
    __many = 0
    __cpu = ""
    __memory = 0
    __time = 0

    def setsize(self, size):
        if size < 6:
            print("你们家有这么小的笔记本吗？拿出来看看？那不出来还写，让你搁这玩呢!!!!")
            p.setsize(int(input("请输入屏幕尺寸：")))
        elif size > 22:
            print("这么大的电脑你怎么带着，怎么不买个电视带着！！")
            p.setsize(int(input("请输入屏幕尺寸：")))
        else:
            self.__size = size

    def getsize(self):
        return self.__size

    def setmany(self, many):
        self.__many = many

    def getmany(self):
        return self.__many

    def setcpu(self, cpu):
        self.__cpu = cpu

    def getcpu(self):
        return self.__cpu

    def setmemory(self, memory):
        if memory <= 0:
            print("你输入的内存是什么玩意，你电脑是废了吗？")
            p.setmemory(int(input("请输入内存大小：")))
        elif memory < 64:
            print("你们家笔记本全是内存吗？？？有这么大的吗？？？")
            p.setmemory(int(input("请输入内存大小：")))
        else:
            self.__memory = memory

    def getmemory(self):
        return self.__memory

    def settime(self, time):
        if time <= 0:
            print("谁家的电脑这么厉害，没有的电池吗？？？？？？？")
            p.settime(int(input("请输入待机时长，注意：是不插电的时长：")))
        else:
            self.__time = time

    def gettime(self):
        return self.__time

    def typewriter(self):

        print("你用", self.__size, "寸屏幕", self.__many, "元", "cpu为", self.__cpu,
              "内存为", self.__memory, self.__time, "小时的待机时长的电脑，你竟然打字！！！")

    def game(self, games):
        print("你用", self.__size, "寸屏幕", self.__many, "元", "cpu为", self.__cpu,
              "内存为", self.__memory, self.__time, "小时的电脑", "打", games, "游戏")

    def look(self, looks):
        print("你用", self.__size, "寸屏幕", self.__many, "元", "cpu为", self.__cpu,
              "内存为", self.__memory, self.__time, "小时的电脑", "看", looks)


p = computer()
p.setsize(int(input("请输入屏幕尺寸：")))
p.setmany(input("请输入购买价格："))
p.setcpu(input("请输入CPU型号："))
p.setmemory(int(input("请输入内存大小：")))
p.settime(int(input("请输入待机时长，注意：是不插电的时长：")))
p.typewriter()
p.game(input("请输入你玩耍的游戏："))
p.look(input("请输入你看的电影："))
