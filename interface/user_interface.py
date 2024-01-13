'''
用户相关接口
'''
from db import db_hander
def register_interface(username,password,balance=0,is_admin=False):
    '''
    注册接口
    :param username:
    :param password:
    :param balance:
    :param is_admin:
    :return:
    '''
    #1 调用数据层查询用户数据是否存在
    #1.1 不存在返回 False
    if  db_hander.select_data(username,data=False):
        return False,'用户数据已经存在'

    #1.2 存在 组织用户数据
    else:
        user_data = {
            'username': username,
            'password': password,
            'balance': balance,
            'shopping_cart': {},
            'flow': [],
            'is_admin': is_admin,
            'locked': False,
        }
        db_hander.save(user_data)
        return True,f'{username} 注册成功！'


def login_inerface(username):
