from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_restx import Api, Resource
from app.main.controller.fileController import FileController

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록
api.add_namespace(FileController, '/file')


@app.route('/index', methods=['GET', 'POST'])
# HTML 렌더링
def index_page():
    return render_template('index.html')


@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
# rest api 요청 추가
class index(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {"hello": "world!"}  # 즉, jsonify를 따로 사용하지 않아도 된다.

    def post():
        return render_template('index.html')


@api.route('/hello/<string:name>')  # url pattern으로 name 설정
class Hello(Resource):
    def get(self, name):  # 멤버 함수의 파라미터로 name 설정
        return {"message": "Welcome, %s!" % name}


@app.route('/fileUpload', methods=['GET', 'POST'])
# 파일 업로드 처리
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        # 유니코드 지원안하는듯 파일명 한글일경우 오류남
        f.save('./uploads/' + secure_filename(f.filename))
        return '업로드 완료'


# 서버 실행
if __name__ == '__main__':
    app.run(host='localhost', port=9080, debug=True)
