from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db, User, Region, Scenic, Travelog, Log
from app.utils import admin_required

admin_bp = Blueprint('admin', __name__)

# 管理员登录
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        if username == 'admin' and pwd == 'admin':
            session['admin_id'] = 1
            log = Log(action='管理员登录', user_type='admin', user_id=1)
            db.session.add(log)
            db.session.commit()
            flash('登录成功')
            return redirect(url_for('admin.dashboard'))
        flash('管理员账号或密码错误')
    return render_template('admin/login.html')

# 后台首页
@admin_bp.route('/')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

# 会员管理
@admin_bp.route('/members')
@admin_required
def members():
    users = User.query.all()
    return render_template('admin/members.html', users=users)

@admin_bp.route('/member/<int:user_id>/delete')
@admin_required
def member_delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('会员已删除')
    return redirect(url_for('admin.members'))

# 地区管理
@admin_bp.route('/regions')
@admin_required
def regions():
    regions = Region.query.all()
    return render_template('admin/regions.html', regions=regions)

# 新增地区
@admin_bp.route('/region/add', methods=['GET', 'POST'])
@admin_required
def region_add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        new_region = Region(name=name, description=description)
        db.session.add(new_region)
        db.session.commit()
        flash('地区添加成功')
        return redirect(url_for('admin.regions'))
    return render_template('admin/region_add.html')

# 编辑地区
@admin_bp.route('/region/<int:region_id>/edit', methods=['GET', 'POST'])
@admin_required
def region_edit(region_id):
    region = Region.query.get_or_404(region_id)
    if request.method == 'POST':
        region.name = request.form['name']
        region.description = request.form.get('description', '')
        db.session.commit()
        flash('地区更新成功')
        return redirect(url_for('admin.regions'))
    return render_template('admin/region_edit.html', region=region)

# 删除地区
@admin_bp.route('/region/<int:region_id>/delete')
@admin_required
def region_delete(region_id):
    region = Region.query.get_or_404(region_id)
    db.session.delete(region)
    db.session.commit()
    flash('地区已删除')
    return redirect(url_for('admin.regions'))

# 景区管理
@admin_bp.route('/scenics')
@admin_required
def scenics():
    scenics = Scenic.query.all()
    regions = Region.query.all()
    return render_template('admin/scenics.html', scenics=scenics, regions=regions)

# 新增景区
@admin_bp.route('/scenic/add', methods=['GET', 'POST'])
@admin_required
def scenic_add():
    regions = Region.query.all()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        region_id = request.form.get('region_id', type=int)
        new_scenic = Scenic(name=name, description=description, region_id=region_id)
        db.session.add(new_scenic)
        db.session.commit()
        flash('景区添加成功')
        return redirect(url_for('admin.scenics'))
    return render_template('admin/scenic_add.html', regions=regions)

# 编辑景区
@admin_bp.route('/scenic/<int:scenic_id>/edit', methods=['GET', 'POST'])
@admin_required
def scenic_edit(scenic_id):
    scenic = Scenic.query.get_or_404(scenic_id)
    regions = Region.query.all()
    if request.method == 'POST':
        scenic.name = request.form['name']
        scenic.description = request.form.get('description', '')
        scenic.region_id = request.form.get('region_id', type=int)
        db.session.commit()
        flash('景区更新成功')
        return redirect(url_for('admin.scenics'))
    return render_template('admin/scenic_edit.html', scenic=scenic, regions=regions)

# 删除景区
@admin_bp.route('/scenic/<int:scenic_id>/delete')
@admin_required
def scenic_delete(scenic_id):
    scenic = Scenic.query.get_or_404(scenic_id)
    db.session.delete(scenic)
    db.session.commit()
    flash('景区已删除')
    return redirect(url_for('admin.scenics'))

# 游记管理
@admin_bp.route('/travelogs')
@admin_required
def travelogs():
    travelogs = Travelog.query.all()
    return render_template('admin/travelogs.html', travelogs=travelogs)

# 新增游记
@admin_bp.route('/travelog/add', methods=['GET', 'POST'])
@admin_required
def travelog_add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form.get('content', '')
        new_travelog = Travelog(title=title, content=content)
        db.session.add(new_travelog)
        db.session.commit()
        flash('游记添加成功')
        return redirect(url_for('admin.travelogs'))
    return render_template('admin/travelog_add.html')

# 编辑游记
@admin_bp.route('/travelog/<int:travelog_id>/edit', methods=['GET', 'POST'])
@admin_required
def travelog_edit(travelog_id):
    travelog = Travelog.query.get_or_404(travelog_id)
    if request.method == 'POST':
        travelog.title = request.form['title']
        travelog.content = request.form.get('content', '')
        db.session.commit()
        flash('游记更新成功')
        return redirect(url_for('admin.travelogs'))
    return render_template('admin/travelog_edit.html', travelog=travelog)

# 删除游记
@admin_bp.route('/travelog/<int:travelog_id>/delete')
@admin_required
def travelog_delete(travelog_id):
    travelog = Travelog.query.get_or_404(travelog_id)
    db.session.delete(travelog)
    db.session.commit()
    flash('游记已删除')
    return redirect(url_for('admin.travelogs'))

# 日志管理
@admin_bp.route('/logs')
@admin_required
def logs():
    logs = Log.query.all()
    return render_template('admin/logs.html', logs=logs)

# 修改密码
@admin_bp.route('/change_password', methods=['POST'])
@admin_required
def change_password():
    flash('密码已修改')
    return redirect(url_for('admin.dashboard'))
