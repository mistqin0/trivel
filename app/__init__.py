from flask import Flask
from config import Config
from app.models import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    
    # 确保实例文件夹存在
    import os
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
        
    db.init_app(app)
    
    # 注册蓝图
    from app.routes.auth import auth_bp
    from app.routes.frontend import frontend_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(frontend_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app

