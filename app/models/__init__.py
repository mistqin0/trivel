
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 必须在 db 定义之后再导入模型，避免循环依赖
from app.models.user import User
from app.models.region import Region
from app.models.scenic import Scenic
from app.models.travelog import Travelog
from app.models.log import Log

