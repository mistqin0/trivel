from app.models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    favorites = db.Column(db.Text) # 存储收藏的景区ID，逗号分隔
    suggestions = db.Column(db.Text) # 意见建议

