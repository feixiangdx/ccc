from threading import Thread
import time

egg = 0

aaa = 0  # 状态


class cook(Thread):
    username = ""

    def run(self) -> None:
        global egg
        while True:
            if aaa == 6:
                print("没钱还想买蛋挞，滚蛋！！！")
                break
            else:
                if egg == 500:
                    time.sleep(3)
                else:
                    egg = egg + 1
                    print(f"{self.username}做了{egg}个蛋挞")


class BuyEgg(Thread):
    name = ""
    money = 3000
    count = 0

    def run(self) -> None:
        global aaa
        global egg
        while True:
            if egg > 0:

                if self.money == 0:
                    print(f"您的资金不足，{self.name}一共获得{self.count}个蛋挞")
                    aaa = aaa + 1
                    break
                else:
                    self.money = self.money - 2
                    self.count = self.count + 1
                    egg = egg - 1
                    print(f"{self.name}买了一个蛋挞")
            else:
                time.sleep(2)
                print(f"{self.name}获得蛋挞{self.count}")


u1 = cook()
u2 = cook()
u3 = cook()
c1 = BuyEgg()
c2 = BuyEgg()
c3 = BuyEgg()
c4 = BuyEgg()
c5 = BuyEgg()
c6 = BuyEgg()
u1.username = "aa"
u2.username = "ab"
u3.username = "ac"
c1.name = "cc"
c2.name = "c1c"
c3.name = "c2c"
c4.name = "c3c"
c5.name = "c4c"
c6.name = "c5c"
u1.start()
u2.start()
u3.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
