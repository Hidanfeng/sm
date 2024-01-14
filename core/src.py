'''
用户视图层
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from interface import user_interface, bank_interface,shop_interface
from lib import common

logged_user = None
logged_admin = False

#退出
def sign_out():
    print('\n感谢使用，欢迎下次光临！')
    exit()

#注册
def register(is_admin=False):
    while True:

        #1、让用户输入用户名和密码
        print('\n注册')
        username = input('请输入用户名：>>> ').strip()
        password = input('请输入密码：>>>').strip()
        re_password = input('请确认密码: >>>').strip()
        is_register = input('按任意键确认/n退出：').strip().lower()

        #2、进行简单的逻辑判断
        #2.1 判断用户是否想要退出
        if is_register == 'n':
            break

        #2.2 判断俩次密码是否一致
        if password != re_password:
            print('俩次输入的密码不一致')
            continue

        #2.3 校验用户名和密码是否合法
        import re   #正则校验
        password = common.pwd_to_sha256(password)

        flag,msg = user_interface.register_interface(username,password,is_admin)
        print(msg)
        if flag:
            break

#登录
def login():
    '''
    登录视图
    :param username:
    :param password:
    :return:
    '''
    while True:
        print('\n登录')
        # 1 用户输入用户名和密码
        username = input('请输入用户名：>>> ').strip()
        password = input('请输入密码：>>>').strip()
        is_register = input('按任意键确认/n退出：').strip().lower()

        # 2、进行简单的逻辑判断
        # 2.1 判断用户是否想要退出
        if is_register == 'n':
            break
        # 2 调用接口层看用户是否存在
        password = common.pwd_to_sha256(password)
        flag, mesg,is_admin = user_interface.login_inerface(username,password)
        print(mesg)
        if flag:
            global logged_user,logged_admin
            logged_user = username
            logged_admin = is_admin
            break

#充值
@common.login_auth
def recharge(userame=False):
    '''
    充值功能
    :return:
    '''
    while True:
        balance = input('请输入你要充值的金额：')
        if not balance.isdigit():
            print('请输入数字')
            continue

        if int(balance) == 0:
            print('请输入大于0的数')
            continue
        money = int(balance)
        if not userame:
            userame = logged_user
        flag,mesg = bank_interface.recharge_interface(userame,money)
        print(mesg)
        if flag:
            break

#提现
@common.login_auth
def withdraw():
    while True:
        print('\n提现')
        balance = input('请输入你要提现的金额：')
        if not balance.isdigit():
            print('请输入数字')
            continue

        if int(balance) == 0:
            print('请输入大于0的数')
            continue
        money = int(balance)

        if money < 500:
            print('\n提现的金额不能低于500！')
            continue
        flag,mesg = bank_interface.withdraw_interface(logged_user,money)
        print(mesg)
        if mesg:
            break

#登出
@common.login_auth
def login_out():
    global logged_user, logged_admin
    print(f'{logged_user} 退出成功')
    logged_user = None
    logged_admin = False

#转账
def transfer():
    while True:
        # 要转账的人
        pass









#查看余额
@common.login_auth  # check_balance = login_auth(check_balance)  check_balance = wrapper
def check_balance():
    flag,mesg = bank_interface.check_balance_interface(logged_user)
    print(mesg)



def check_flow():
    pass

#购物功能
def shopping():
    # 1 展示商品列表
    shopinp_car = {}
    # {"韭菜":{"number": "F00001", "name": "韭菜", "price": 2.0, "商品数量": 2},}

    flag, goods = shop_interface.check_goods_interface('goods')
    if not flag:
        print(goods)
        return  #没有商品结束当前购物功能返回主菜单
    while True:
        print('欢迎来到铁牛商城'.center(50, '='))
        print(f'{"序号":<10}{"商品编号":<10}{"商品名称":<10}{"商品价格":<10}')
        for num, good in enumerate(goods):
            print(f'{num+1:<10}{good.get("number"):<10}{good.get("name"):<10}{good.get("price"):<10}')
        print('24小时为您服务'.center(50, '='))
        # 2 用户操作选择
        opt = input('请选择商品序号(y结算/n退出)：').strip()
        # 2.1 选择n退出
        # 2.1.1 shopinp_car = None break
        if opt =='n':
            if not shopinp_car:
                break
            #2.1.2 shopinp_car 不是空
            else:
                flag,mesg = shop_interface.add_shop_cart_interface(logged_user,shopinp_car)
                print(mesg)
                if flag:
                    break

        #3 选择y
        if opt =='y':
            if not shopinp_car:
                print('\n没有选择任何商品，无法结算！')
                break
            #
            flag,mesg,total= shop_interface.close_account_interface(logged_user,shopinp_car)












def check_shopping_cart():
    pass

#管理员功能
def admin():
    from core import admin
    admin.main()



func_dic = {
    '0':('退出',sign_out),
    '1':('注册功能',register),
    '2':('登录功能',login),
    '3':('充值功能',recharge),
    '4':('转账功能',transfer),
    '5':('提现功能',withdraw),
    '6':('查看余额', check_balance),
    '7':('查看流水', check_flow),
    '8':('购物功能', shopping),
    '9':('查看购物车', check_shopping_cart),
    '10':('登出功能',login_out),
    '11':('管理员功能',admin)
}


def main():

    while True:
        print('购物管理系统'.center(20, '='))
        for num in func_dic:
            if logged_admin:
                print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))
            else:
                if num !='11':
                    print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))
        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号').strip()
        if opt not in func_dic or (not logged_admin and opt == '11'):
            print('此功能不存在')
            continue

        func_dic[opt][1]()



main()









