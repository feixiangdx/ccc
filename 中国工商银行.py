import random

print("*************************************")
print("*             中国工商银行          *")
print("*            账户管理系统           *")
print("*                v1.0               *")
print("*************************************")
print("* 1.开户                            *")
print("* 2.存钱                            *")
print("* 3.取钱                            *")
print("* 4.转账                            *")
print("* 5.查询                            *")
print("* 6.ByB!                            *")
print("*************************************")

bank = {}  # 银行的库
bank_name = "中国工商银行昌平分行"


#                 一一对应  ，  不是名称对应
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100: return 3  # bank_adduser=3
    if account in bank: return 2  # bank_adduser=2
    bank[account] = {
        "username": username,  # 键：你输入的值account=random.randint(10000000,99999999)
        "password": password,  # password = input("请输入您的密码")
        "country": country,  # country = input("\t\t请输入您的国家")
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    print(bank)
    return 1  # bank_adduser=1


def adduser():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account = random.randint(10000000, 99999999)
    status = bank_adduser(account, username, password, country, province, street, door)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    账号：%s
                    用户名：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (account, username, country, province, street, door, bank[account]["money"], bank_name))


def save(account, money):  # 存钱
    if account in bank.keys():
        bank[account]["money"] = bank[account]["money"] + money
        print("卡内余额：", bank[account]["money"])
    else:
        print(False)


def withdraw(account, password):  # 取钱
    if account in bank.keys():
        if password == bank[account]["password"]:
            money = input("请输入取出金额：")
            money = int(money)
            if money <= bank[account]["money"]:
                bank[account]["money"] = bank[account]["money"] - money
                print("成功取出：", money)
                print("卡内余额：", bank[account]["money"])
            else:
                print(3)
        else:
            print(2)

    else:
        print(1)


def transfer_accounts(account1, password1, account2, password2):
    if account1 in bank.keys():

        if password1 in bank[account]["password"]:

            if account2 in bank.keys():

                if password2 in bank[account]["password"]:
                    money = input("请输入转出金额：")
                    money = int(money)
                    if money <= bank[account]["money"]:
                        bank[account]["money"] = bank[account]["money"] - money
                        print("成功转出：", money)
                        print("卡内余额：", bank[account]["money"])
                    else:
                        print(3)
                else:
                    print(2)
            else:
                print(1)

        else:
            print(2)
    else:
        print(1)


def pooling(account, password):
    if account in bank.keys():
        if password in bank[account]["password"]:

            print("当前账号：", account)
            print("密码：*******", )
            print("当前余额:", bank[account]["money"])
            print("当前居住地：", bank[account]["country"], bank[account]["province"],
                  bank[account]["street"], bank[account]["door"])
            print("当前开户行：", bank_name)


        else:
            print("密码不正确，你确定是你的卡吗？？？？")
    else:
        print("该用户不存在！！！！！")


while True:
    begin = input("请选择业务:")
    if begin == "1":
        print("1、开户")
        adduser()
    elif begin == "2":
        print("2、存钱")
        account = input("请输入8位账号：")
        account = int(account)
        money = input("请输入存入的钱：")
        money = int(money)
        save(account, money)
    elif begin == "3":
        print("3、取钱")
        account = input("请输入8位账号：")
        account = int(account)
        password = input("请输入密码：")
        withdraw(account, password)
    elif begin == "4":
        print("4、转账")
        account1 = input("请输入转出账号:")
        account1 = int(account1)
        password1 = input("请输入密码：")
        account2 = input("请输入转入账号:")
        account2 = int(account2)
        password2 = input("请输入密码：")
        if account1 == account2:
            print("账号相同，请重试，让你搁这儿玩呢！！")
        else:
            transfer_accounts(account1, password1, account2, password2)
    elif begin == "5":
        print("5、查询 ")
        account = input("请输入账号：")
        account = int(account)
        password = input("请输入密码：")
        pooling(account, password)
    elif begin == "6":
        print("6、退出")
        print("欢迎下次光临！！！")
        break
