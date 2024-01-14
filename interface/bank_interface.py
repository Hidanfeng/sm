'''
银行相关接口
'''
from datetime import datetime

from db import db_hander
from conf import settings

def recharge_interface(username,balance):
    '''
    充值接口
    :param username:
    :param balance:
    :return:
    '''
    user_data = db_hander.select_data(username)
    if not user_data:
        return True,f'{username} 该用户不存在'
    user_data['balance'] += balance
    db_hander.save(user_data)
    return True, f'{username} 充值 {balance} 元，成功！\n 当前余额为{user_data.get("balance")}'

def withdraw_interface(username,amount):
    '''
    提现接口
    :param username:
    :param balance:
    :return:
    '''
    user_data = db_hander.select_data(username)
    #1 账号余额
    balance = user_data.get('balance')
    #2 计算手续费
    service_fee = amount*settings.BANK_RATE

    if balance< amount+service_fee:
        return False,f'{username} 你的账号余额不足'
    #3 提现
    user_data['balance'] -= (amount+service_fee)
    db_hander.save(user_data)
    return True, f'{username} 提现 {balance} 元，成功！\n 当前余额为{user_data.get("balance")}'

def check_balance_interface(username):
    '''
    查看余额接口
    :param username:
    :return:
    '''
    userdata = db_hander.select_data(username)
    if userdata:
        balance = userdata.get('balance')
        return True,f'用户{username} 当前余额为 {balance}'

def transfer():
    '''
    转账功能
    :return:
    '''
    pass


def pay_interface(username,total):
    '''
    支付接口
    :return:
    '''
    # 1、拿到用户数据
    user_data = db_hander.select_data(username)

    # 2、判断用户余额是否充足
    if user_data.get('balance') < total:
        msg = f'用户：{username} 余额不足，支付：{total} 元，失败！'
        return False, msg

    # 3、支付
    user_data['balance'] -= total

    # 5、保存用户数据
    db_hander.save(user_data)
    msg = f'{datetime.now()} 用户：{username} 消费：{total} 元，' \
          f'当前余额为：{user_data.get("balance")}'

    return True, msg