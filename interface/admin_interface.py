'''
管理员接口
'''
from db import db_hander
def lock_user_interface(username):
    '''
    冻结账号接口
    :return:
    '''
    #查要冻结的账号
    user_data = db_hander.select_data(username)
    #如果用户不存在
    if not user_data:
        return False,f'{username} 用户数据不存在'
    #如果账号存在
    if user_data:
        user_data['locked'] = True
    #保存用户数据
    db_hander.save(user_data)
    return True,f'{username} 冻结成功'
