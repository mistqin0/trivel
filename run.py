from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()  # 自动创建数据库表

if __name__ == '__main__':
    app.run(debug=True)

