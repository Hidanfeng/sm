'''
配置信息
'''
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import configparser

CONFIG_PATH = os.path.join(
    BASE_DIR, 'settings.cfg'
)
config = configparser.ConfigParser()
config.read(CONFIG_PATH,encoding='utf-8')

#用户数据存放路径
USER_DATA_DIR = config.get('path','USER_DATA_DIR')
if not os.path.isdir(USER_DATA_DIR):
    USER_DATA_DIR = os.path.join(
        BASE_DIR,'db','user_data'
    )

#商品数据存放路径
GOODS_DATA_DIR = os.path.join(
    BASE_DIR,'db','goods_data'
)

BANK_RATE = config.getfloat('bank','RATE')


