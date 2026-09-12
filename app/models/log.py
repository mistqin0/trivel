from app.models import db

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_type = db.Column(db.String(20)) # admin / user
    user_id = db.Column(db.Integer)

