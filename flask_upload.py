from flask import Flask, render_template
app = Flask(__name__)

#HTML 렌더링
@app.route('/')
def home_page():
	return render_template('index.html')

#서버 실행
if __name__ == '__main__':
	app.run(host='localhost', port=9080, debug = True)