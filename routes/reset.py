import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    abort,
    send_from_directory,
    current_app)

from models.message import Messages
from models.reply import Reply
from models.topic import Topic
from models.user import User
# from routes import current_user, cache
from routes import current_user, new_csrf_token, csrf_required, csrf_tokens

import json

from utils import log

main = Blueprint('reset', __name__)


@main.route("/send", methods=["POST"])
def send():
    form = request.form.to_dict()
    username = form['username']
    user = User.one(username=username)
    # 发邮件
    token = str(uuid.uuid4())
    # 修改token写入方式
    csrf_tokens.set(token, user.id)
    Messages.send(
        title='修改密码地址',
        content='http://49.235.39.104:80/reset/view?token={}&user={}'.format(token, user.username),
        sender_id=user.id,
        receiver_id=user.id,
    )
    # 发送完毕回到登录界面
    return redirect(url_for('index.index'))


@main.route('/reset_view')
def reset_view():
    return render_template('reset_view.html')


@main.route("/view")
def view():
    token = request.args.get('token')
    user = request.args.get('user')
    log('tst1', csrf_tokens)
    return render_template('reset.html', token=token, user=user)


@main.route("/update", methods=["POST"])
# 无法使用装饰器的token鉴别
def update():
    form = request.form.to_dict()
    username = request.args.get('user')
    user = User.one(username=username)
    token = request.args.get('token')
    # 修改判断方式
    if csrf_tokens.exists(token):
        user_id = csrf_tokens.get(token)
        if user.id == user_id:
            csrf_tokens.delete(token)
    password = form['password']
    password = User.salted_password(password)
    user.update(user.id, password=password)
    return render_template('index.html')