from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

# 用户登录
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user = User.query.filter_by(username=username, password=pwd).first()
        if user:
            session['user_id'] = user.id
            flash('登录成功')
            return redirect(url_for('frontend.index'))
        flash('用户名或密码错误')
    return render_template('auth/login.html')

# 用户注册
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('用户名已存在')
            return redirect(url_for('auth.register'))
        user = User(username=username, password=pwd)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，请登录')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

# 退出登录
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('frontend.index'))

