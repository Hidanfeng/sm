'''
用户相关接口
'''
from db import db_hander

def register_interface(username, password, balance=0, is_admin=False):
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


def login_inerface(username,password):
    '''
    登录接口
    :param username:
    :param password:
    :return:
    '''
    #1 查看用户是否存在 需要返回数据data 判断用户名和密码是否匹配
    user_data = db_hander.select_data(username)
    #1.1 用户不存在
    if not user_data:
        return False, f'{username} 用户数据不存在,请重新输入', False
    #1.2 用户存在
    if not password == user_data['password']:
        return False, f'{username} 用户密码输入有误,请重新输入！', False
    if user_data['locked']:
        return False, f'{username} 用户被冻结了！'
    return True, f'{username} 登录成功！',user_data['is_admin']

