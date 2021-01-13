# flask_file_upload
flask 파일업로드 서버(vue.js 연동예정)

frontend, backend 동시 구동가능한 환경 만드는게 아주 번거로워서 그냥 분리하기로함
backend 구조는 flask프로젝트가 처음이라 아래 flask-restx의 보일러플레이트 소스 참고하여
MVC패턴 폴더구조로 생성

#### FLASK RESTX BOILER-PLATE WITH JWT

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.

### Full description and guide ###
https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563


### Contributing
If you want to contribute to this flask restplus boilerplate, clone the repository and just start making pull requests.

```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git
```
