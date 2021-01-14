from flask_restx import Api
from flask import Blueprint

from .main.controller.fileController import api as file_ns
from .main.controller.deepLearningController import api as dl_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.view_controller import api as view_ns
# -> 각 controller에서 만든 api 함수를 가져와서 아래 blueprint에 등록해서 사용가능하도록

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0', description='파이썬(flask) API 서버 입니다.')

api.add_namespace(file_ns, path='/file')
api.add_namespace(dl_ns, path='/dl')
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(view_ns)
