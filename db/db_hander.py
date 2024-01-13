'''
数据处理层
'''
import os
from  conf import settings
import json

def select_data(username,data=True):
    '''

    :param username:
    :param data:  如果需要用户数据 data就不用户传值，如果不需要data就传Falue
    :return:
    '''
    #1、接收接口层过来的username 并拼接用户名.json
    user_path = os.path.join(
        settings.USER_DATA_DIR, f'{username}.json'
    )
    #2、判断用户是否存在
    #2.1 用户不存在
    if not os.path.exists(user_path):
        return
    #2.2 用户存在 不用返回数据
    if not data:
        return True
    #2.3 用户存在 要返回数据
    with open(user_path,'rt',encoding='utf-8')as f:
        user_data = json.load(f)
        return user_data



def save(userdata):
    user_path = os.path.join(
        settings.USER_DATA_DIR, f'{userdata["username"]}.json'
    )
    with open(user_path,'wt',encoding='utf-8')as f:
        json.dump(userdata,f,ensure_ascii=False)
        return True
