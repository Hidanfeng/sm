'''
用户视图层
'''
import os
from interface import user_interface
logged_user = None
logged_admin = False

def sign_out():
    print('\n感谢使用，欢迎下次光临！')
    exit()


def register():
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

        flag,msg = user_interface.register_interface(username,password)
        print(msg)
        if flag:
            break






def login(username,password):
    '''
    登录视图
    :param username:
    :param password:
    :return:
    '''





func_dic = {
    '0':('退出',sign_out),
    '1':('注册功能',register),
    '2':('登录功能',login)
}


def main():

    while True:
        print('购物管理系统'.center(20, '='))
        for num in func_dic:
            print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))
        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号').strip()
        if opt not in func_dic:
            print('此功能不存在')
            continue
        else:
            func_dic.get(opt)[1]()




if __name__ == '__main__':
    main()








