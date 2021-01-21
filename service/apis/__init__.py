from flask_restplus import Api
from service import app


api = Api(
    app,
    version='0.0.1',
    title='volunteer_management',
    description='志愿者信息管理api',
    # authorizations={},  # 认证
    ui=True,
)

from service.apis.volunteers import *