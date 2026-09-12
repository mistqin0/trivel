from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db, Scenic, Region, Travelog, User

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    scenics = Scenic.query.limit(5).all()
    regions = Region.query.limit(5).all()
    return render_template('frontend/index.html', scenics=scenics, regions=regions)

@frontend_bp.route('/scenics')
def scenic_list():
    scenics = Scenic.query.all()
    return render_template('frontend/scenics.html', scenics=scenics)

@frontend_bp.route('/scenic/<int:id>')
def scenic_detail(id):
    scenic = Scenic.query.get_or_404(id)
    travelogs = Travelog.query.all()
    return render_template('frontend/scenic_detail.html', scenic=scenic, travelogs=travelogs)

@frontend_bp.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    fav_ids = [int(i) for i in user.favorites.split(',') if i.isdigit()] if user.favorites else []
    fav_scenics = Scenic.query.filter(Scenic.id.in_(fav_ids)).all()
    return render_template('frontend/favorites.html', fav_scenics=fav_scenics)

@frontend_bp.route('/collect/<int:scenic_id>')
def collect(scenic_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    favs = user.favorites.split(',') if user.favorites else []
    favs.append(str(scenic_id))
    user.favorites = ','.join(set(favs))
    db.session.commit()
    flash('收藏成功')
    return redirect(url_for('frontend.scenic_list'))

@frontend_bp.route('/about')
def about():
    return render_template('frontend/about.html')

