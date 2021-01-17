from flask_restx import Namespace, Resource, fields
from flask import request
from werkzeug.utils import secure_filename

api = Namespace("file", description="file related operations")

@api.route("/upload")
class file(Resource):
    @api.doc("upload_file")
    def post(self):
        files = request.files
        # 저장할 경로 + 파일명
        # 유니코드 지원안하는듯 파일명 한글일경우 오류남
        # print(type(files))
        # print(files)
        for f in files.to_dict(flat=False)['file']:
            f.save('./uploads/'+secure_filename(f.filename))
            print(f.filename)
        return {"result": "success"}
