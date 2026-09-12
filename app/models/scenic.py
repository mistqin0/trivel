from app.models import db

class Scenic(db.Model):
    __tablename__ = 'scenics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))

