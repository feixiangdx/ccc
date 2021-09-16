import pymysql
import random
menu = '''
*************************************
*             中国工商银行          *
*            账户管理系统           *
*                v1.0               *
*************************************
* 1.开户                            *
* 2.存钱                            *
* 3.取钱                            *
* 4.转账                            *
* 5.查询                            *
* 6.ByB!                            *
*************************************
'''

info = '''
        -------------用户信息--------------------
        账号：{}
        用户名：{}
        密码：******
        国家：{}
        省份：{}
        街道：{}
        门牌号：{}
        余额：{}
        开户行：{}
'''

uid_list = []
bank_name = "中国工商银行昌平分行"


def mysql():
    conn = pymysql.connect(host="localhost", user='root', password='', database='bank')
    cursor = conn.cursor()
    return cursor, conn


def get_account(cur):
    cur.execute(
        """select account from usuer"""
    )
    data = cur.fetchall()
    for d in data:
        uid_list.append(d[0])


def close_mysql(cur, conn):
    cur.close()
    conn.close()


def add_user(t_dict):
    cur, conn = mysql()
    get_account(cur)
    if t_dict['account'] in uid_list:
        return 2
    else:
        if len(uid_list) == 100:
            return 3
        else:
            cur.execute(
                """insert into usuer(account,username,password,country,province,street,door,deposit,bank_name)
                value(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (t_dict['account'], t_dict['username'], t_dict['password'], t_dict['country'], t_dict['province'],
                 t_dict['street'], t_dict['door'], t_dict['deposit'], bank_name)
            )
            conn.commit()
            close_mysql(cur, conn)
            return 1


def save_money(account, money):
    cur, conn = mysql()
    get_account(cur)
    cur.execute(
        """select deposit from usuer where account=%s""",
        account
    )
    deposit = cur.fetchone()
    money += deposit[0]
    if account in uid_list:
        cur.execute(
            """update usuer set deposit=%s where account=%s""",
            (deposit[0] + money, account)
        )
        conn.commit()
        close_mysql(cur, conn)
        return True
    else:
        return False


def withdraw_money(account, password, money):
    cur, conn = mysql()
    get_account(cur)
    cur.execute(
        """select password,deposit from usuer where account=%s""",
        account
    )
    data = cur.fetchone()
    if account in uid_list:
        if password == data[0]:
            if money <= data[1]:
                cur.execute(
                    """update usuer set deposit=%s where account=%s""",
                    (data[1] - money, account)
                )
                conn.commit()
                close_mysql(cur, conn)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def transfer(out_id, in_id, out_passwd, money):
    cur, conn = mysql()
    get_account(cur)
    cur.execute(
        """select password,deposit from usuer where account=%s""",
        out_id
    )
    out_data = cur.fetchone()
    cur.execute(
        """select deposit from usuer where account=%s""",
        in_id
    )
    in_data = cur.fetchone()
    if out_id and in_id in uid_list:
        if out_passwd == out_data[0]:
            if money <= out_data[1]:
                cur.execute(
                    """update usuer set deposit=%s where account=%s""",
                    (out_data[1] - money, out_id)
                )
                cur.execute(
                    """update usuer set deposit=%s where account=%s""",
                    (in_data[0] + money, in_id)
                )
                conn.commit()
                close_mysql(cur, conn)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def usuer(account, password):
    cur, conn = mysql()
    get_account(cur)
    cur.execute(
        """select * from usuer where account=%s""",
        account
    )
    data = cur.fetchone()
    if account in uid_list:
        if password == data[2]:
            print(info.format(data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8]))
        else:
            print("密码错误")
    else:
        print("该用户不存在")


if __name__ == '__main__':
    print(menu)
    while True:
        sel = int(input("请输入业务编号："))
        if sel == 1:
            account = str(random.randint(10000000, 99999999))  # zfill(8)的作用就是当字符串不够8位时，在首位填充0
            name = input("请输入用户姓名：")
            password = input("请输入用户密码(6位数字)：")
            print("请输入用户地址：")
            country = input("\t\t请输入国家：")
            province = input("\t\t请输入省份：")
            street = input("\t\t请输入街道：")
            door = input("\t\t请输入门牌号：")
            temp = {'account': account, 'username': name, 'password': password, 'country': country, 'province': province,
                    'street': street, 'door': door, 'deposit': 0}
            result = add_user(temp)
            if result == 1:
                print("用户添加成功，用户信息如下")
                print(info.format(account, name, country, province, street, door, 0, bank_name))
            elif result == 2:
                print("用户账号已存在，请重新操作")
            elif result == 3:
                print("用户库注册已满，无法添加新用户")
        elif sel == 2:
            account = int(input("请输入用户账号："))
            money = float(input("请输入存入金额："))
            re = save_money(account, money)
            if re:
                print("存入成功")
            else:
                print("没有此用户，请检查用户账号")
        elif sel == 3:
            account = int(input("请输入用户账号："))
            passwd = input("请输入用户密码：")
            withdraw = float(input("请输入取钱金额："))
            r = withdraw_money(account, passwd, withdraw)
            if r == 1:
                print("用户不存在，请检查用户账号")
            elif r == 2:
                print("密码错误，请检查用户密码")
            elif r == 3:
                print("存款不足，请检查取出金额")
            else:
                print("取出成功")
        elif sel == 4:
            out_account = int(input("请输入转出账号："))
            in_account = int(input("请输入转入账号："))
            out_passwd = input("请输入转出账号密码：")
            money = float(input("请输入转出金额："))
            res = transfer(out_account, in_account, out_passwd, money)
            if res == 1:
                print("用户不存在，请检查转入和转出账号")
            elif res == 2:
                print("密码不正确，请检查转出账号密码")
            elif res == 3:
                print("存款不足，请检查转出金额")
            else:
                print("转账成功")
        elif sel == 5:
            account = int(input("请输入用户账号："))
            passwd = input("请输入用户密码：")
            usuer(account, passwd)
        elif sel == 6:
            print("再见,不用再来了")
            break
        else:
            print("输入错误，请检查编号")
