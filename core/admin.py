'''
管理员视图
'''
#添加用户
from core import src
from interface import admin_interface
def add_user():
    print('\n添加用户')
    is_admin = input('是否添加管理员(y or n):').strip().lower()
    if is_admin == 'y':
        src.register(is_admin=True)
    else:
        src.register(is_admin=False)

#冻结账号功能
def lock_user():
    while True:
        print('\n冻结账号功能')
        to_lock_user = input('请输入你要冻结的账号').strip()
        flag,mesg = admin_interface.lock_user_interface(to_lock_user)
        print(mesg)
        if flag:
            break


def recharge_to_user():
    print('\n给用户充值')
    usename = input('请输入你要充值的用户名').strip()
    src.recharge(usename)


func_dic = {
    '0': ('返回首页',),
    '1': ('添加账户', add_user),
    '2': ('冻结账户', lock_user),
    '3': ('给用户充值', recharge_to_user)
}


# 管理员视图层的主程序
def main():
    while True:
        print('管理员功能'.center(20, '='))
        for num in func_dic:
            print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))
        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号：').strip()
        if opt not in func_dic:
            print('此功能不存在！')
            continue
        if opt == '0':
            break
        func_dic.get(opt)[1]()
