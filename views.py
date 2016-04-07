# coding:utf-8

from config import *
from flask import Flask, flash, render_template, request, session, redirect, url_for, abort
from database import db_session
from models import User, Post
import datetime

app = Flask(__name__)

@app.route('/register', methods=['POST', 'GET'])
def register():
    errormsg = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        obj = User.query.filter_by(username=username).first()
        if obj:
            errormsg = u'该用户名已被注册'
        else:
            user = User(username=username, password=password)
            db_session.add(user)
            db_session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', errormsg=errormsg)

@app.route('/login', methods=['POST', 'GET'])
def login():
    errormsg = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            errormsg = u'用户名不存在'
        elif not user.check_password(password):
            errormsg = u'密码错误'
        else:
            session['username'] = user.username
            flash(u'登录时间为:%s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return redirect(url_for('index'))
    return render_template('login.html', errormsg=errormsg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    posts = Post.query.order_by('update_time desc').limit(10)
    for post in posts:
        print post.title
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host=RUN_HOST, port=RUN_PORT, debug=DEBUG)
