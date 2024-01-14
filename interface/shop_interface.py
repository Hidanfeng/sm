'''
购物相关的接口
'''
from db import db_hander
from interface import bank_interface

#展示商品列表接口
def check_goods_interface(good):
    goods_data = db_hander.select_data(good,is_user=False)
    if not goods_data:
        return False,f'商品列表为空'
    if goods_data:
        return True,goods_data


#添加购物车接口
def add_shop_cart_interface(username, shopping_cart):
    '''
    添加用户购物车功能
    :param username:
    :param shopping_cart:
    :return:
    '''
    #获取用户购物车数据
    user_data = db_hander.select_data(username)
    shopping_cart_list = user_data.get('shopping_cart')
    #判断商品名称是否在用户的购物车中 如果在 数量相加 不再直接加进去
    for name in shopping_cart.keys():
        if name in shopping_cart_list:
            shopping_cart_list[name]['数量'] += shopping_cart.get(name).get('数量')
        else:
            shopping_cart_list[name] = shopping_cart.get(name)
    #保存数据
    user_data['shopping_cart'] = shopping_cart_list
    db_hander.save(user_data)
    return True,f'用户：{username} 购物车添加成功！'

#结算接口
def close_account_interface(username, shopping_cart):
    total = 0
    for good_info in shopping_cart.values():
        price = good_info.get('price')
        num = good_info.get('数量')
        total += price*num
    flag, msg = bank_interface.pay_interface(username,total)
    return flag, msg, total






