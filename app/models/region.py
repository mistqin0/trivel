from app.models import db

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    scenics = db.relationship('Scenic', backref='region', lazy=True)
    description=db.Column(db.Text)
