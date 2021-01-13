from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

#HTML 렌더링
@app.route('/')
def index_page():
	return render_template('index.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		#저장할 경로 + 파일명
		f.save('./uploads/' + secure_filename(f.filename)) # 유니코드 지원안하는듯 파일명 한글일경우 오류남
		return render_template('index.html')

#서버 실행
if __name__ == '__main__':
	app.run(host='localhost', port=9080, debug = True)