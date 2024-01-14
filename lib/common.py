'''
公共方法
'''

# 登录认证装饰器
def login_auth(fuc):
    from core import src
    def wrapper(*args,**kwargs):

        if src.logged_user:
            res = fuc(*args,**kwargs)
            return res
        else:
            print('你个憨憨，还没有登录呢！')
            src.login()

    return wrapper



# 密码加密
def pwd_to_sha256(password):
    import hashlib
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    sha.update('接着奏乐接着舞'.encode('gbk'))
    return sha.hexdigest()