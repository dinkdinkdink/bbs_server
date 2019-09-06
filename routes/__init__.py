import uuid
from functools import wraps

import redis
from flask import request, abort

from models.user import User
from utils import log
import json


session = redis.StrictRedis()


def current_user():
    if 'session_id' in request.cookies:
        session_id = request.cookies['session_id']
        key = 'session_id_{}'.format(session_id)
        user_id = int(session.get(key))
        log('current_user key <{}> user_id <{}>'.format(key, user_id))
        u = User.one(id=user_id)
        return u
    else:
        return None

# def current_user():
#     uid = session.get('user_id', '')
#     u: User = User.one(id=uid)
#     # type annotation
#     # User u = User.one(id=uid)
#     return u


csrf_tokens = redis.StrictRedis()


# 修改装饰器
def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args['token']
        u = current_user()
        if csrf_tokens.exists(token):
            user_id = csrf_tokens.get(token)
            if u.id == user_id:
                csrf_tokens.delete(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


# 修改创建函数
def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    log('tst', token, type(token))
    result = csrf_tokens.set(token, u.id)
    log('test1', result)
    return token


cache = redis.StrictRedis()