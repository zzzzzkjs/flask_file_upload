from flask_restx import Namespace, Resource, fields

api = Namespace("file", description="file related operations")

# 요청 methods설정 할수있는지 확인 필요


@api.route("/upload")
class file(Resource):
    @api.doc("upload_file")
    def upload(self):
        """List all dogs"""
        return {'resultCode': '0000', 'resultMessage': '정상처리'}

# #파일 업로드 처리
# @app.route('/fileUpload', methods = ['GET', 'POST'])
# def upload_file():
# 	if request.method == 'POST':
# 		f = request.files['file']
# 		#저장할 경로 + 파일명
# 		f.save('./uploads/' + secure_filename(f.filename)) # 유니코드 지원안하는듯 파일명 한글일경우 오류남
# 		return '업로드 완료'
